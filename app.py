import streamlit as st
from langchain.llms import CTransformers 
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import SemanticSimilarityExampleSelector
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os
import torch  # Import torch for GPU handling
import numpy as np
import time  # Import the time module
import re
from sqlalchemy.exc import SQLAlchemyError  # Import SQLAlchemy error handling

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# Initialize the LLM
def initialize_llm():
    llm = CTransformers(
        model="model\original-metallama-6epoch-graphofloss-2.Q4_1.gguf",
        model_type="llama", 
        config={'max_new_tokens': 110, 'temperature': 0.5, 'context_length': 2990}
    )
    return llm

# Set page configuration
st.set_page_config(page_title="Chat-Gossip", page_icon="💬", layout="wide")

# Custom CSS for chat-like conversation and overall appearance
st.markdown("""
    <style>
    .stApp {
        background-color: #202123;
        color: white;
    }
    .user-bubble {
        background-color: #15ad6e;
        border-radius: 12px;
        padding: 8px;
        margin: 5px -200px;
        max-width: 80%;
    }
    .ai-bubble {
        background-color: #0995ad;
        border-radius: 12px;
        padding: 8px;
        margin: 5px -200px;
        max-width: 80%;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        max-width: 600px;
        margin: 0 auto;
    }
    .user-bubble-container {
        align-items: flex-end;
        justify-content: flex-end;
        margin-bottom: 22px;
    }
    .ai-bubble-container {
        align-items: flex-start;
        justify-content: flex-start;
        margin-bottom: 22px;
    }
    .input-container {
        display: flex;
        justify-content: center;
        padding: 10px;
    }
    .input-container .stTextInput {
        width: 100%; 
    }
    .input-container .stButton {
        display: flex;
        justify-content: center;
        width: 100%; 
    }
    </style>
    """, unsafe_allow_html=True)

# Centered header
st.markdown("<h3 style='text-align: center; color: #ad9f09;'>Welcome to personalized ChatGpt</h3>", unsafe_allow_html=True)

# Database and embeddings setup
username = 'root'
password = 'prabal9869'
host = '127.0.0.1'
dbname = 'arl_bank2'
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=3)
CHROMA_DIR = "vectorstore/chroma"
CHROMA_DB_PATH = os.path.join(CHROMA_DIR, "index")

if not os.path.exists(CHROMA_DB_PATH):
    try:
        os.makedirs(CHROMA_DIR, exist_ok=True)
        st.write(f"Directory created or already exists: {CHROMA_DIR}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')
few_shots = [
    {
        'Question': "How much amount did I earn last year?",
        'SQLQuery': """SELECT SUM(Deposit_amount) AS Earned FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE) - 1;""",
        'SQLResult': "1542",
        'Answer': "You earned Rs 1,542 last year."
    }
    ,
    {
    'Question': "How many transactions did I make each day this week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, COUNT(*) AS Total_Transactions
                   FROM transactions
                   WHERE YEARWEEK(Value_date) = YEARWEEK(CURRENT_DATE())
                   GROUP BY DATE(Value_date)""",
    'SQLResult': "78",
    'Answer': "You made 78 transactions this week."
},
  {
    'Question': "Give me the breakdown of my income of each month this year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Income
                   FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) GROUP BY YEAR(Value_date), MONTH(Value_date)""",
    'SQLResult': """[(2024,1, Decimal('10133087.00')),
        (2024,2, Decimal('15161439.00')),
        (2024,3, Decimal('12471013.00')),
        (2024,4, Decimal('12207818.00')),
        (2024,5, Decimal('13288480.00'))]""",
    'Answer': """Here is your breakdown of your income of each month this year.
    2024 January: Rs 1,01,33,087 ,
    2024 February: Rs  1,51,61,439 ,
    2024 March: Rs  1,24,71,013 ,
    2024 April: Rs  1,22,07,818 ,
    2024 May: Rs  1,32,88,480"""
},
{
    'Question': "In which category did i spend the most money this month ?",
    'SQLQuery': """SELECT Transaction_details AS Category, SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND MONTH(Value_date) = MONTH(CURRENT_DATE()) GROUP BY Transaction_details ORDER BY Total_Spending DESC LIMIT 1;""",
    'SQLResult': "[Healthcare, Decimal('10133087.00'))]",
    'Answer': "You spend most money on Healthcare which is Rs 1,01,33,087.00 this month ."
}
]

if os.path.exists(CHROMA_DB_PATH):
    st.write("Loading embeddings from existing Chroma vector store.")
    vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
else:
    st.write("Creating new embeddings and saving to Chroma vector store.")
   
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots, persist_directory=CHROMA_DB_PATH)
    vectorstore.persist()

example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=1,
)

mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run.
Table information:Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

Table information:
1. `transactions` with columns: `Account_No`, `Date`, `Transaction_details`, `Value_date`, `Withdrawal_amount`, `Deposit_amount`, `Balance_amount`."""
example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=mysql_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

new_chain = SQLDatabaseChain.from_llm(llm=initialize_llm(), db=db, verbose=True, prompt=few_shot_prompt)

# sentence-transformers/all-mpnet-base-v2
# sentence-transformers/all-MiniLM-L6-v2
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
example_questions = [shot['Question'].strip() for shot in few_shots]
example_embeddings = model.encode(example_questions)

def is_question_relevant(user_question, similarity_threshold=0.50):
    user_embedding = model.encode([user_question])[0]
    similarity_scores = cosine_similarity(user_embedding.reshape(1, -1), example_embeddings)[0]
    max_similarity_score = max(similarity_scores)
    print(f"Max Similarity Score: {max_similarity_score}")  # Add this line for debugging
    return max_similarity_score > similarity_threshold

# Modify the handle_user_query function to handle exceptions
def handle_user_query(user_question):
    if is_question_relevant(user_question):
        try:
            # Attempt to generate the response from the LLM and SQL database
            return new_chain.run(user_question)
        # except SQLAlchemyError as e:
        #     # Catch SQLAlchemy errors and return a generic message
        #     # st.error("Sorry, I am unable to respond.")
        #     return "Sorry, I am unable to respond."
        except Exception as e:
            print(f"Error occurred: {e}")  # Add this line for debugging
            # Catch any other exceptions and return a generic message
            # st.error("Sorry, I am unable to respond.")
            return "Sorry, I am unable to respond."
    else:
        return "Sorry I cannot answer your Question."

# Load LLM
llm = initialize_llm()

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Chat functionality with Streamlit
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! I am your personal ChatGpt.🤗"]

if 'past' not in st.session_state:
    st.session_state['past'] = [" Hey! 👋"]

response_container = st.container()

# Adjust container for input field to mimic ChatGPT style
with st.container():
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

    with col2:  # Center column for the input
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input(
                "Query:",
                placeholder="Ask about your bank transactions here (:",
                key='input',
                label_visibility="collapsed"
            )
            submit_button = st.form_submit_button(label='Send')

    st.markdown("</div>", unsafe_allow_html=True)

    if submit_button and user_input:
        st.session_state['past'].append(user_input)  # Display user's question immediately
        start_time = time.time()  # Start the timer

        with st.spinner("Generating response..."):
            response = handle_user_query(user_input)
            if response == "Sorry, I am unable to respond.":
                st.session_state['generated'].append(response)
            else:
                end_time = time.time()  # Stop the timer
                elapsed_time = end_time - start_time  # Calculate elapsed time
                # Define the patterns to split on
                patterns = [r'\nQuestion', r'\nAnswer', r'\n\nQuestion','\nQuestion','A']

                # Join the patterns into a single regular expression
                combined_pattern = '|'.join(patterns)

                # Use re.split to split based on any of the patterns
                split_response = re.split(combined_pattern, response, maxsplit=1)
                extracted_result = split_response[0].strip() if split_response else response.strip()

                # Append the result with the elapsed time
                st.session_state['generated'].append(f"{extracted_result} (Generated in {elapsed_time:.2f} seconds)")

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            user_msg = st.session_state['past'][i]
            ai_msg = st.session_state['generated'][i]
            
            # Display user and AI messages
            st.markdown(f"""
                <div class='chat-container user-bubble-container'>
                    <div class='user-bubble'>{user_msg}</div>
                </div>
                <div class='chat-container ai-bubble-container'>
                    <div class='ai-bubble'>{ai_msg}</div>
                </div>
                """, unsafe_allow_html=True)
