# Resume-Analyzer
Resume Analyzer – ATS Compatibility & Resume Evaluation Tool

A web-based application that analyzes resumes against job descriptions to estimate ATS (Applicant Tracking System) compatibility, evaluate keyword relevance, and provide actionable resume improvement insights using NLP techniques.

This project is designed to help students, job seekers, and professionals understand how resume screening systems work and optimize their resumes accordingly.

Key Features :

1. ATS Compatibility Score
Estimates how well a resume may perform during ATS-based screening.
2. Resume vs Job Description Matching
Compares resume content with a given job description to identify relevance gaps.
3. Keyword Analysis
Highlights missing, weak, or underrepresented keywords important for the target role.
4. Resume Text Extraction
Extracts and preprocesses text from PDF resumes.
5. Interactive Web Interface
Simple and user-friendly UI for uploading resumes and viewing results.

Tech Stack :

> Programming Language: Python
> Core Concepts: Natural Language Processing (NLP)
> Libraries & Tools:
> Streamlit (Web Interface)
> Scikit-learn (Text Vectorization & Similarity Analysis)
> NLTK (Text Preprocessing)
> PyPDF2 (PDF Text Extraction)

How the System Works :

1. User uploads a resume (PDF format).
2. User pastes a target job description.
3. The system preprocesses both texts (cleaning, tokenization, normalization).
4. NLP techniques are applied to compare resume and job description content.
5. An ATS compatibility score and improvement insights are generated.
