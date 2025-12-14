🚀 AI Resume Enhancer (GenAI + ATS)

An end-to-end Generative AI–powered Resume Enhancement Platform that analyzes resumes against job descriptions, predicts an ATS score, identifies skill gaps, and generates an AI-improved resume downloadable as PDF or DOCX.

This project demonstrates practical use of LLMs, NLP, embeddings, and product-level thinking, making it highly suitable for AI / GenAI / Data Science internship applications.

✨ Key Features

📄 Resume Upload Support (PDF & DOCX)

🧠 LLM-powered Resume Enhancement

📊 Single ATS Score Prediction

🎯 Skill Gap Analysis (Resume vs Job Description)

✍️ AI-Generated Improved Resume

⬇️ Download Improved Resume (PDF / DOCX)

🌐 Browser-based UI using Streamlit

🧩 Problem Statement

Many candidates fail to receive interview calls because their resumes are not optimized for:

Applicant Tracking Systems (ATS)

Job-specific keywords

Clear, impact-driven bullet points

This tool solves that problem by using Generative AI + NLP to transform resumes into ATS-optimized, recruiter-friendly documents.

🏗️ System Architecture
User (Browser)
   ↓
Streamlit Frontend
   ↓
Resume Parser (PDF/DOCX)
   ↓
NLP + Skill Extraction
   ↓
ATS Scoring Engine
   ↓
LLM Resume Enhancement
   ↓
PDF / DOCX Generator
🛠️ Tech Stack
Core Technologies

Python 3.10

Streamlit – Web Interface

OpenAI / LLM API – Resume Enhancement

Sentence Transformers – Skill Matching (optional)

NLP & Document Handling

nltk

scikit-learn

python-docx

PyPDF2

reportlab

📂 Project Structure
AI-resume-enhancer/
│
├── app.py              # Streamlit frontend
├── backend.py          # Core NLP + LLM logic
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/sravan-jetangula/AI-resume-enhancer.git
cd AI-resume-enhancer
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set OpenAI API Key

Windows (PowerShell):

setx OPENAI_API_KEY 

Restart terminal after setting the key.

▶️ Run the Application
streamlit run app.py

Open in browser:

http://localhost:8501
📊 Output Details
ATS Score

Single combined ATS score (0–100)

Based on keyword match + readability

Skill Gap Analysis

Resume skills

Job-required skills

Missing skills (if any)

AI-Improved Resume

Strong action verbs

Job-aligned bullet points

Downloadable as PDF or DOCX

🎯 Why This Project Stands Out

✔ Real-world HR Tech problem ✔ Applied Generative AI (not theory) ✔ End-to-end product mindset ✔ Recruiter-friendly use case ✔ Deployable web application

This project is highly impactful for resumes targeting:

GenAI Intern

AI Engineer Intern

Data Science Intern

NLP Engineer Intern

🚀 Future Enhancements

Agentic AI resume optimization loop

Job scraping from LinkedIn/Internshala

Resume version comparison

Cover letter generator

Multi-language resume support

👨‍💻 Author

Jetangula Sravan Kumar
B.Tech – Artificial Intelligence & Machine Learning
Aspiring GenAI & AI Engineer

🔗 GitHub: https://github.com/sravan-jetangula

📜 License

This project is licensed for educational and portfolio use.

⭐ If you find this project useful, please star the repository!
