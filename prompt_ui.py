from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

load_dotenv()

st.header("Research Tool")

user_input = st.text_input("Enter your prompt ")

if st.button("Summarize"):
    result= model.invoke(user_input)
    st.write(result.content)
