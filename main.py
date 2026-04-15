import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are an expert educator on human trafficking prevention in the UK.

Explain clearly and safely in both English and Italian:
1. How recruiters groom and manipulate young women in the UK
2. Common tactics used
3. Systems used (social media, fake jobs, etc.)
4. Provide a SAFE realistic scenario
5. Give warning signs and prevention advice

Keep it educational and protective. Structure the response with English first, followed by the Italian translation.
""")

def generate_lesson():
    messages = prompt.format_messages()
    response = llm(messages)
    return response.content


# UI
st.title("Human Trafficking Awareness (UK)")

if st.button("Tell me how recruiters groom young women in the UK"):
    with st.spinner("Generating..."):
        lesson = generate_lesson()
        st.markdown(lesson)