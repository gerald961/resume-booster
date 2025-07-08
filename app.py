import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from feedback_engine import analyze_resume

st.set_page_config(page_title="Resume Booster", layout="wide")
st.title("📄 Resume Booster")
st.subheader("Upload your resume to get AI-powered feedback")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    st.text_area("Parsed Resume Text", resume_text, height=300)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing..."):
            feedback = analyze_resume(resume_text)
            st.markdown("### 📋 AI Feedback")
            st.markdown(feedback)
