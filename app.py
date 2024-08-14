# to load the fine tuned model
from langchain.llms import CTransformers 
from langchain_community.utilities import SQLDatabase   #To interact with the database
from langchain_experimental.sql import SQLDatabaseChain #To create a chain of llm and database chain
from langchain.embeddings import HuggingFaceEmbeddings  #To load the embedding model from hugging face
from langchain.vectorstores import Chroma               #Chroma Vectorstore
from langchain.prompts import FewShotPromptTemplate     #To create fewshot template that servers as reference for the llm
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX,_mysql_prompt 
from langchain.prompts.prompt import PromptTemplate     #Prompt template for llm input
from sentence_transformers import SentenceTransformer   #To load the embedding model
from guardrails import Guard, OnFailAction              #To implement guardrails 
from guardrails.hub import CompetitorCheck, ToxicLanguage
from guardrails.hub import ProfanityFree
from sklearn.metrics.pairwise import cosine_similarity  
import streamlit as st
import os
from langchain.prompts import SemanticSimilarityExampleSelector



# Function for Loading the model from the local storage
# def load_llm():
llm = CTransformers(model="model\original-metallama-5epoch-graphofloss.Q5_0.gguf",
                        model_type="llama", config={'max_new_tokens':40,'temperature':0.5,'context_length': 3990})
    # return llm

st.title("Welcome to chat-chat-chat-gossip")
# Mark down
st.markdown("<h3 style='text-align: center; color: green;'>Guff garam ekxin aau</h3>",
            unsafe_allow_html=True)
# MySQL connection URI
username = 'root'  #username 
password = 'prabal9869' #password
host = '127.0.0.1'  #host
dbname = 'arl1_bank'  # Database name

# Constructing the MySQL URI
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

# # Initializing SQLDatabase object for MySQL
db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=3)
# print(db.table_info)
#Creating a database chain
db_chain = SQLDatabaseChain.from_llm(llm=llm,db=db,verbose=True)
few_shots= [
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


# Define the path to save the vector store
CHROMA_DIR = "vectorstore/chroma"
CHROMA_DB_PATH = os.path.join(CHROMA_DIR, "index")

if not os.path.exists(CHROMA_DB_PATH):
    try:
        # Ensure the vectorstore directory exists
        os.makedirs(CHROMA_DIR, exist_ok=True)
        st.write(f"Directory created or already exists: {CHROMA_DIR}")
    except FileNotFoundError as e:
        print(f"Error creating directory: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
# Check if the vector store already exists
if os.path.exists(CHROMA_DB_PATH):
    st.write("Loading embeddings from existing Chroma vector store.")
    
    vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
else:
    st.write("Creating new embeddings and saving to Chroma vector store.")
    # Create embeddings and vector store
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots, persist_directory=CHROMA_DB_PATH)
    vectorstore.persist()
    print(f"New embeddings created and saved at: {CHROMA_DB_PATH}")

#Selecting the most appropriate example from vectorstore that servers as reference for llm to generate response to unseen user questions
example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=1,
)
st.write(example_selector.select_examples({"Question":"What is my income last month?"}))
mysql_prompt = """You are an expert in converting natural language questions into MySQL queries. Your task is to generate a syntactically correct MySQL query based on the given input question, execute the query, and then provide an answer based on the query results.
Here is the database schema defined by create statement. CREATE TABLE transactions ( `Account_No` VARCHAR(50) NOT NULL, `Transaction_details` TEXT, `Withdrawal_amount` INTEGER, `Deposit_amount` INTEGER, `Balance_amount` INTEGER, `Value_date` DATE, `Date` DATE )
Pay attention to use CURDATE() function to get the current date, if the question involves "today","this year","this month" ,"this week","last month","last week","last year".
Pay attention to only answer the single question of the user at a time ."""
#Creating a format for the generating the reponse
example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)
#Formatting the fewshot template
few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=mysql_prompt,
    suffix="Question: {input} ",
    input_variables=["input","top_k"], #These variables are used in the prefix and suffix
)
new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
example_questions = [shot['Question'].strip() for shot in few_shots]
print(example_questions)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
example_embeddings = model.encode(example_questions)

# Function to determine if a user question is relevant to the database context
def is_question_relevant(user_question, similarity_threshold=0.40):
    user_embedding = model.encode([user_question])[0]  
    
    # calculating the cosine similarity between user question and example questions
    similarity_scores = cosine_similarity(user_embedding.reshape(1, -1), example_embeddings)[0]
    print(similarity_scores)
    
    max_similarity_score = max(similarity_scores)
    print(max_similarity_score)
    return max_similarity_score > similarity_threshold

#Setting uo the guard rail for profanity,toxiclanguage etc.
guard = Guard().use_many(
    CompetitorCheck(["khalti", "fusemachine","Deerhold","Deerwalk","Cotiviti"], on_fail=OnFailAction.EXCEPTION),
    ToxicLanguage(threshold=0.9, validation_method="sentence", on_fail=OnFailAction.EXCEPTION),
    ProfanityFree(on_fail=OnFailAction.EXCEPTION))

# Function to handle user queries
def handle_user_query(user_question):
    if is_question_relevant(user_question):
        return True
    else:
        return "Your Question is not Relevant to the Context"
    
# User question in natural language
user_question = "What is my current net worth for account number 409000493201 ?"
print(user_question)

try:
    # Validate the user question
    guard.validate(user_question)  # If validation fails, an exception will be thrown
    # If validation passes, handle the user query
    response = handle_user_query(user_question)
except Exception as e:
    response = str(e)

if response==True:
    result=new_chain(user_question)
    st.write(result)
else:
    print(response)