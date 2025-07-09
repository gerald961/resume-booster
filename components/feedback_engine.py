import streamlit as st
from openai import OpenAI
from components.prompt_templates import resume_feedback_prompt
from config import MODEL, TEMPERATURE


# Initialize OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_resume(text):
    prompt = resume_feedback_prompt.format(resume_text=text)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE
    )
    
    return response.choices[0].message.content.strip()
