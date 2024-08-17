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
import numpy as np
import time  # Import the time module

# Initialize the LLM
def initialize_llm():
    llm = CTransformers(model="model\original-metallama-5epoch-graphofloss.Q4_1.gguf",
                        model_type="llama", 
                        config={'max_new_tokens': 100, 'temperature': 0.5, 'context_length': 3990})
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
    }
    .user-bubble-container {
        align-items: flex-end;
        display: flex;
        justify-content: flex-end;
    }
    .ai-bubble-container {
        align-items: flex-start;
        display: flex;
        justify-content: flex-start;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #ad9f09;'>Welcome to personalized ChatGpt</h3>", unsafe_allow_html=True)

# Database and embeddings setup
username = 'root'
password = 'prabal9869'
host = '127.0.0.1'
dbname = 'arl1_bank'
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
    'Question': "How much amount did i earned last year ?",
    'SQLQuery': """SELECT SUM(Deposit_amount) AS Earned FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE) - 1;"""
    ,
    'SQLResult': "1542",
    'Answer': "You made 1542 transactions this year. </s>"
},
{
    'Question': "I want to buy a car worth RS. 5,00,000 in next 2 years . So how much should i save each month to buy the car . ",
    'SQLQuery': """SELECT round(AVG(Monthly_Savings),0) AS Average_Monthly_Savings FROM (SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, SUM(Deposit_amount - Withdrawal_amount) AS Monthly_Savings FROM transactions GROUP BY YEAR(Value_date), MONTH(Value_date)) AS Monthly_Savings_Calculation;""",
    'SQLResult': """9385""",
    'Answer': """So your average monthly saving is RS 9385 .
    Lets think step by step:
        step-1) Determine Total Number of Months:
        Time frame: 2 years (12 months in 1 year So 2 years * 12 months = 24) = 24 months
    step-2) Calculate Required Monthly Savings:
        Target amount: RS 500000
        Required monthly savings:(It is obtained by dividing the total amount by Time frame) i.e RS. 500000 / 24 months = RS. 20,833.33
    step-3) Compare Current Savings with Required Savings:
        Current average monthly savings: RS 9385
        Difference needed:  RS 20,833.33 - RS 9385 = RS. 11,448.33
    step-4) Conclusion: To reach the goal of saving RS 500,000 in 2 years. increase monthly savings to RS 20,833.33 .The additional amount to save each month is RS. 11,448.33 </s>"""
}
,
{
    'Question': "Can you give me a short description about my spendings of this month ?",
    'SQLQuery': """SELECT COUNT(*) AS number_of_transactions,SUM(Withdrawal_amount) AS total_spending,MAX(Withdrawal_amount) AS highest_transaction_amount FROM transactions WHERE year(Value_date) =year(curdate()) And month(value_date) = month(curdate()) ;"""
    ,
    'SQLResult': """[(Decimal('2772')),
                    (Decimal('529053340')),
                    (Decimal('10000000')),
                    ( Decimal('0'))]""",
    'Answer': "You made 2772 transaction , spend RS 529,053,340 in total , RS 10,000,000 and RS 0 was you highest and lowest spending of this month .  </s>"
}
,
 {
    'Question': "What was my net worth for account number x in year 2022 ? ",
    'SQLQuery': """SELECT Balance_amount AS Net_Worth FROM transactions where account_no='x' and year(value_date)='2022' ORDER BY Value_date DESC LIMIT 1; """,
    'SQLResult':'1283234',
    'Answer':"Your networth in 2022 was RS 12,83,234"
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

mysql_prompt = """You are an expert in converting natural language questions into MySQL queries. Your task is to generate a syntactically correct MySQL query based on the given input question, execute the query, and then provide an answer based on the query results.
Here is the database schema defined by create statement. CREATE TABLE transactions ( `Account_No` VARCHAR(50) NOT NULL, `Transaction_details` TEXT, `Withdrawal_amount` INTEGER, `Deposit_amount` INTEGER, `Balance_amount` INTEGER, `Value_date` DATE, `Date` DATE )
Pay attention to use CURDATE() function to get the current date, if the question involves "today","this year","this month" ,"this week","last month","last week","last year".
Pay attention to only answer the single question of the user at a time ."""
example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=mysql_prompt,
    suffix="Question: {input} ",
    input_variables=["input"],
)

new_chain = SQLDatabaseChain.from_llm(llm=initialize_llm(), db=db, verbose=True, prompt=few_shot_prompt)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
example_questions = [shot['Question'].strip() for shot in few_shots]
example_embeddings = model.encode(example_questions)

def is_question_relevant(user_question, similarity_threshold=0.40):
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
    st.session_state['past'] = ["Hey! 👋"]

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Ask about your bank transactions here (:", key='input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        st.session_state['past'].append(user_input)  # Display user's question immediately
        start_time = time.time()  # Start the timer

        with st.spinner("Generating response..."):
            response = handle_user_query(user_input)
            if response == True:
                res = new_chain.run(user_input)
                end_time = time.time()  # Stop the timer
                elapsed_time = end_time - start_time  # Calculate elapsed time
                extracted_result = res.split('\n')[0].strip()
                st.session_state['generated'].append(f"{extracted_result} (Generated in {elapsed_time:.2f} seconds)")
            else:
                st.error(response)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            user_msg = st.session_state['past'][i]
            ai_msg = st.session_state['generated'][i]
            
            st.markdown(f"<div class='chat-container user-bubble-container'><div class='user-bubble'>{user_msg}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-container ai-bubble-container'><div class='ai-bubble'>{ai_msg}</div></div>", unsafe_allow_html=True)
