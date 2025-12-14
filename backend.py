import pdfplumber
import docx2txt
import re
from fpdf import FPDF

# -------------------- LOAD RESUME --------------------

def load_resume(file):
    ext = file.name.split(".")[-1].lower()

    if ext == "pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text

    elif ext == "docx":
        return docx2txt.process(file)

    return ""


# -------------------- ATS SCORE --------------------

def calculate_ats_score(resume_text, job_text):
    resume_words = set(re.findall(r"[a-zA-Z+#.]+", resume_text.lower()))
    job_words = set(re.findall(r"[a-zA-Z+#.]+", job_text.lower()))

    matched = resume_words.intersection(job_words)
    score = round((len(matched) / max(len(job_words), 1)) * 100, 2)

    return score


# -------------------- SKILL EXTRACTION --------------------

def extract_skills(text):
    skill_bank = [
        "python", "machine learning", "deep learning", "nlp",
        "data science", "model fine-tuning", "llm",
        "ai", "ml", "recommendation", "document parsing"
    ]
    text = text.lower()
    return sorted({s for s in skill_bank if s in text})


# -------------------- RESUME IMPROVER (LOCAL AI STYLE) --------------------

def improve_resume(resume_text, job_text):
    skills = extract_skills(job_text)

    improved = f"""
PROFESSIONAL SUMMARY
AI/ML-focused candidate with strong foundations in Machine Learning, Deep Learning, NLP, and AI system development.
Experienced in building data-driven applications and optimizing models for real-world use cases.

CORE SKILLS
{", ".join(skills)}

PROJECT HIGHLIGHTS
- Designed AI-driven pipelines using NLP and ML techniques.
- Built resume analysis and recommendation-style systems.
- Worked on document parsing and automated text processing.

EXPERIENCE & LEARNING
- Applied ML and DL algorithms to practical datasets.
- Improved model reliability through evaluation and iteration.

ORIGINAL RESUME CONTENT
{resume_text}
"""
    return improved.strip()


# -------------------- PDF GENERATION (UNICODE SAFE) --------------------

def generate_pdf(text, output="Improved_Resume.pdf"):
    def clean(txt):
        replacements = {
            "•": "-",
            "–": "-",
            "—": "-",
            "“": '"',
            "”": '"',
            "’": "'",
            "‘": "'"
        }
        for k, v in replacements.items():
            txt = txt.replace(k, v)
        return txt.encode("latin-1", "ignore").decode("latin-1")

    text = clean(text)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(output)
    return output
