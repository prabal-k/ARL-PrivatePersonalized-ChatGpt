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

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# Initialize the LLM
def initialize_llm():
    llm = CTransformers(
        model="model\original-metallama-6epoch-graphofloss-2.Q4_1.gguf",
        model_type="llama", 
        config={'max_new_tokens': 280, 'temperature': 0.5, 'context_length': 3990}
    )
    if device == "cuda":
        llm.model.to(device)  # Move the model to GPU if available
    return llm

# Set page configuration with a different background color
st.set_page_config(page_title="Chat-Gossip", page_icon="💬", layout="wide")

# Custom CSS for chat-like conversation and background color
st.markdown("""
    <style>
    .stApp {
        background-color: #202123;
    }
    .user-bubble {
        background-color: #15ad6e;
        border-radius: 12px;
        padding: 8px;
        margin: 5px 0;
        max-width: 80%;
    }
    .ai-bubble {
        background-color: #0995ad;
        border-radius: 12px;
        padding: 8px;
        margin: 5px 0;
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
        margin-bottom: 8px;
    }
    .ai-bubble-container {
        align-items: flex-start;
        justify-content: flex-start;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

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

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
few_shots = [
    {
        'Question': "How much amount did I earn last year?",
        'SQLQuery': """SELECT SUM(Deposit_amount) AS Earned FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE) - 1;""",
        'SQLResult': "1542",
        'Answer': "You earned Rs 1,542 last year ."
    },
    {
    'Question': "What is my total spending on utilities this month?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Utilities_Spending
                   FROM transactions
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE())
                   AND Transaction_details = 'Utilities';"""
      ,
    'SQLResult': "23142",
    'Answer': "Your total spending on utilities this month is Rs 23,142 ."
},
 {
    'Question': "I want to buy a car worth RS 6,00,000 in next 3 years . So how much should i save each month to buy the car ?  ",
    'SQLQuery': """SELECT AVG(Monthly_Savings) AS Average_Monthly_Savings FROM (SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month,SUM(Deposit_amount - Withdrawal_amount) AS Monthly_Savings FROM transactions GROUP BY YEAR(Value_date), MONTH(Value_date)) AS Monthly_Savings_Calculation;""",
    'SQLResult': """9627.44""",
    'Answer': """Lets think step by step:
        step-1) Determine Total Number of Months:
        Time frame: 3 years (12 months in 1 year So 3 years * 12 months = 36) = 36 months

    step-2) Calculate Required Monthly Savings:
        Target amount: RS 6,00,000
        Required monthly savings:(It is obtained by dividing the total amount by Time frame)RS 600000 / 36 months = RS 16,666.67

    step-3) Compare Current Savings with Required Savings:
        Current average monthly savings: RS 9627.44
        Difference needed: RS 16,666.67 - RS 9,627.44 = RS 7,039.23

    step-4) Conclusion: To reach the goal of saving RS 6,00,000 in 3 years, increase monthly savings to RS 16,666.67 The additional amount to save each month is RS 7,039.23"""
},
 {
        'Question':"What is my total expenses of last 8 months ?",
        'SQLQuery':"""SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 8 MONTH);""",
        'SQLResult':"75124046",
        'Answer':"Your expenses of last 8 months is Rs 75,124,046 "
    },
    {
        'Question':"How much did I save last month ?",
        'SQLQuery':"""SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Savings_Last_Month FROM 
transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE() - INTERVAL 1 MONTH) AND MONTH(Value_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH);""",
        'SQLResult':"-193509",
        'Answer':"You saved -193509 last month."
    },


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

mysql_prompt = """You are an expert in converting natural language questions into MySQL queries. The question involves "today","this year","this month" ,"this week","last month","last week","last year".
Pay attention to only answer the single question of the user at a time."""
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

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
example_questions = [shot['Question'].strip() for shot in few_shots]
example_embeddings = model.encode(example_questions)

def is_question_relevant(user_question, similarity_threshold=0.50):
    user_embedding = model.encode([user_question])[0]
    similarity_scores = cosine_similarity(user_embedding.reshape(1, -1), example_embeddings)[0]
    max_similarity_score = max(similarity_scores)
    return max_similarity_score > similarity_threshold

# Handle user query function
def handle_user_query(user_question):
    if is_question_relevant(user_question):
        return True
    else:
        return "Your question is not relevant to the context."

# Load LLM
llm = initialize_llm()

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Chat functionality with Streamlit
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! I am your personal CHATGPT. You can ask me anything about your finance 🤗"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["🤖 , Hey! 👋"]

response_container = st.container()

# Adjust container for input field to mimic ChatGPT style
with st.container():
    with st.form(key='my_form', clear_on_submit=True):
        # Center the input field and limit its width
        user_input = st.text_input(
            "Query:",
            placeholder="Ask about your bank transactions here (:",
            key='input',
            label_visibility="collapsed"
        )
        # Center the submit button and input field
        submit_button = st.form_submit_button(label='Send')

        # Custom CSS for narrowing and centering the input field and submit button
        st.write("""
            <style>
            div.stTextInput > div {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0 auto;
                width: 50%;
            }
            div.stTextInput input {
                width: 70%;
                max-width: 400px;
            }
            button[kind=primary] {
                margin-top: 0px;  /* Reduced margin */
                margin-left: 10px; /* Move button closer to input */
                padding: 0.5rem 1rem;
                width: auto;
                display: inline-block;
            }
            </style>
            """, unsafe_allow_html=True)

    if submit_button and user_input:
        st.session_state['past'].append(user_input)  # Display user's question immediately
        start_time = time.time()  # Start the timer

        with st.spinner("Generating response..."):
            response = handle_user_query(user_input)
            if response == True:
                res = new_chain.run(user_input)
                end_time = time.time()  # Stop the timer
                elapsed_time = end_time - start_time  # Calculate elapsed time
                extracted_result = res.split('\n\nQuestion')[0].strip()
                st.session_state['generated'].append(f"{extracted_result} (Generated in {elapsed_time:.2f} seconds)")
            else:
                st.session_state['generated'].append(f"{response}")

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            user_msg = st.session_state['past'][i]
            ai_msg = st.session_state['generated'][i]
            
            # Custom CSS for chat bubbles
            st.markdown(f"""
                <div class='chat-container user-bubble-container'>
                    <div class='user-bubble' style='max-width: 500px; margin-bottom: 8px;'>{user_msg}</div>
                </div>
                <div class='chat-container ai-bubble-container'>
                    <div class='ai-bubble' style='max-width: 500px; margin-bottom: 8px;'>{ai_msg}</div>
                </div>
                """, unsafe_allow_html=True)

# Custom CSS for overall page and chat bubble styling
st.write("""
    <style>
    .stApp {
        background-color: #202123;
    }
    .user-bubble {
        background-color: #15ad6e;
        border-radius: 12px;
        padding: 8px;
        margin: 5px 0;
        max-width: 80%;
    }
    .ai-bubble {
        background-color: #0995ad;
        border-radius: 12px;
        padding: 8px;
        margin: 5px 0;
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
        margin-bottom: 8px;
    }
    .ai-bubble-container {
        align-items: flex-start;
        justify-content: flex-start;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
