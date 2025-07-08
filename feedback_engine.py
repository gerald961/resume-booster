import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def analyze_resume(text):
    prompt = f'''
You are a resume coach for early-career professionals. Here's a resume:

{text}

Give:
1. 3 strengths
2. 3 areas to improve
3. Overall score (out of 100) with reasoning
'''

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()
