import streamlit as st
from backend import load_resume, calculate_ats_score, improve_resume, generate_pdf

st.set_page_config(page_title="AI Resume Enhancer", layout="wide")
st.title(" AI Resume Enhancer ")

resume_file = st.file_uploader(" Upload Your Resume (PDF / DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description", height=220)

if st.button("Analyze & Improve Resume"):
    if not resume_file or not job_desc.strip():
        st.error("Please upload a resume and paste job description.")
    else:
        with st.spinner("Processing resume..."):
            resume_text = load_resume(resume_file)
            ats_score = calculate_ats_score(resume_text, job_desc)
            improved_resume = improve_resume(resume_text, job_desc)
            pdf_path = generate_pdf(improved_resume)

        st.success("Analysis Complete ")

        st.subheader(" ATS Score")
        st.metric("ATS Compatibility", f"{ats_score}%")

        st.subheader(" Improved Resume Preview")
        st.text_area("", improved_resume, height=400)

        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Download Improved Resume (PDF)",
                f,
                file_name="Improved_Resume.pdf",
                mime="application/pdf"
            )
