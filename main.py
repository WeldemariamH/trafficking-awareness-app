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
    google_api_key=st.secrets["GOOGLE_API_KEY"]
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are an expert educator on human trafficking prevention in the UK.

STRICT RULES:
- Do NOT include hashtags
- Do NOT include emojis
- Do NOT add any extra commentary or introduction
- Do NOT repeat information
- Keep the content concise and clear
- Use ONLY bullet points (no long paragraphs)

TASK:
Explain safely and educationally:

1. How recruiters groom and manipulate young women in the UK
2. Common tactics used
3. Systems used (e.g., social media, fake jobs)
4. Provide one SAFE and realistic example scenario
5. Give warning signs and prevention advice

OUTPUT FORMAT (follow exactly):

## English

### Grooming Methods
- ...
- ...

### Common Tactics
- ...
- ...

### Systems Used
- ...
- ...

### Example Scenario
- ...

### Warning Signs & Prevention
- ...
- ...

---

## Italian

(Provide the same sections translated into Italian, keeping bullet points)

IMPORTANT:
- Keep structure identical in both languages
- Do NOT add anything outside this format
""")

def generate_lesson():
    messages = prompt.format_messages()
    response = llm.invoke(messages)
    return response.content[0]["text"]


# UI
st.title("Human Trafficking Awareness (UK)")

if st.button("Tell me how recruiters groom young women in the UK"):
    with st.spinner("Generating..."):
        lesson = generate_lesson()
        st.markdown(lesson)