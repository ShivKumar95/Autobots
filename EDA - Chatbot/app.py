import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.openai import ChatOpenAI
from langchain.experimental.agents import create_pandas_dataframe_agent
from langchain.prompts import PromptTemplate
# importing openai key from .env file and csv/excel from user
load_dotenv()
OPENAI_KEY  = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
st.set_page_config(page_title="DataFrame Agent", layout="wide")
st.title("DataFrame Agent with LangChain and Streamlit")

st.sidebar.header("Upload your Data File")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

df = None
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        st.write("DataFrame Preview:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error loading file: {e}")

# System instructions input
st.sidebar.header("System Instructions")
default_instructions = "You are a helpful assistant that answers questions about the provided DataFrame."
system_instructions = st.sidebar.text_area("Enter system instructions:", value=default_instructions, height=100)
# Chat UI
if "history" not in st.session_state:
    st.session_state.history = []

user_query = st.text_input("Enter your question about the DataFrame:")
if user_query and df is not None:
    with st.spinner("Processing..."):
        llm = ChatOpenAI(model="gpt-4.1-mini",temperature=0.5, openai_api_key=OPENAI_KEY)
        agent = create_pandas_dataframe_agent(
            llm, 
            df,
            agent_type="tool-calling", 
            verbose=True,
            allow_intermediate_steps=True,
            alow_dangerous_code_execution=True,
            system_message = system_instructions)
        try:
            answer = agent.execute(user_query)
        except Exception as e:
            answer = f"Error processing query: {e}"
        st.session_state.history.append(("user", user_query))
        st.session_state.history.append(("assistant", answer))
elif user_query and df is None:
    st.error("Please upload a CSV or Excel file to proceed.")

# Display chat history
for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Assistant:** {msg}")

