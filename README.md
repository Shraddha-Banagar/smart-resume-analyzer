# Smart Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions using Natural Language Processing (NLP) techniques such as TF-IDF and Cosine Similarity. The system calculates a match score and suggests missing skills to improve job alignment.

---

##  Project Overview

Smart Resume Analyzer helps job seekers evaluate how well their resume matches a specific job description. It extracts text from uploaded resumes, compares it with job requirements, and provides a match percentage along with suggested missing keywords.

This project demonstrates practical implementation of NLP concepts in a real-world application.

---

##  Features

- Upload Resume (PDF format)
- Extract and preprocess resume text
- Compare resume with job description
- Calculate match percentage
- Suggest missing keywords
- Clean and professional user interface

---

##  Tech Stack

- **Frontend:** HTML5, CSS3
- **Backend:** Python, Flask
- **Libraries:** 
  - Scikit-learn
  - NLTK 
  - PyPDF2 / pdfplumber (for PDF extraction)
- **NLP Techniques:**
  - TF-IDF Vectorization
  - Cosine Similarity

---

##  How It Works

1. User uploads a resume (PDF).
2. Text is extracted from the resume.
3. Job description is taken as input.
4. Both texts are converted into numerical vectors using TF-IDF.
5. Cosine similarity is calculated between the vectors.
6. Match score is displayed along with missing keywords.

---
## 📂 Project Structure

```
smart-resume-analyzer/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```
---

##  Installation & Setup

1. Clone the repository
2. Install required libraries:
   pip install -r requirements.txt
3. Run the application:
   python app.py
4. Open in browser:
   http://127.0.0.1:5000/


