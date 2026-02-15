from flask import Flask, render_template, request
import os
import PyPDF2
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords (only first time)
nltk.download('stopwords')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Predefined skills database
SKILLS_DB = [
    "python", "sql", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "flask",
    "tensorflow", "keras", "power bi", "tableau",
    "excel", "nlp", "statistics", "scikit-learn",
    "git", "github", "html", "css", "react"
]

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Preprocess text
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

# Calculate similarity
def calculate_similarity(text1, text2):
    if text1.strip() == "" or text2.strip() == "":
        return 0.0
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return similarity[0][0]

# Extract skills
def extract_skills(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return found_skills

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    matched_skills = []
    missing_skills = []

    if request.method == 'POST':
        uploaded_file = request.files['resume']
        job_description = request.form['job_description']

        if uploaded_file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)

            raw_resume = extract_text_from_pdf(file_path)
            clean_resume = preprocess_text(raw_resume)
            clean_job_desc = preprocess_text(job_description)

            # Extract skills first
            resume_skills = extract_skills(clean_resume)
            job_skills = extract_skills(clean_job_desc)

            matched_skills = list(set(resume_skills) & set(job_skills))
            missing_skills = list(set(job_skills) - set(resume_skills))

            # Convert skill lists into text
            resume_skills_text = " ".join(resume_skills)
            job_skills_text = " ".join(job_skills)

            # Calculate similarity using SKILLS ONLY
            similarity_score = calculate_similarity(resume_skills_text, job_skills_text)
            score = round(similarity_score * 100, 2)

    return render_template(
        'index.html',
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )

if __name__ == '__main__':
    app.run(debug=True)
