import streamlit as st
from sklearn .feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

#NLTK Resources

nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger_eng")

#page setup

st.set_page_config(page_title="ATS Resume Analyzer",page_icon="🪼",layout="wide")

st.markdown("""
Check Your Resume's **ATS Compatibility**.  
Upload your resume and paste a job description to get an ATS score.
""")

with st.sidebar:
    st.header("ABOUT")
    st.info(""" 
            This tool helps you with:
            - Measures how your resume matches a job description
            - Identify important job keywords
            - Reduce chances of instant rejection
            """)
    st.header("HOW IT WORKS")
    st.write(""" 
            1. Upload your resume (PDF)
            2. Paste the job description
            3. Click **"CHECK"**
            """)
 
#Functions

def extract_text_from_pdf(upload_pdf):
    try:
        pdf_reder=PyPDF2.PdfReader(upload_pdf)
        text=""
        for page in pdf_reder.pages:
            text=text+page.extract_text()
        return text
    except Exception as e:
        st.error(f"error reading PDF :{e}")
        return ""

def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z\s]','',text)
    text=re.sub(r'\s+',' ',text).strip()
    return text

def remove_stopwords(text):
    stop_words=set(stopwords.words('english'))
    words=word_tokenize(text)
    return " ".join([word for word in words if word not in stop_words])

def cal_sim(resume_text,job_desc):
    processed_resume=remove_stopwords(clean_text(resume_text))
    processed_job_desc=remove_stopwords(clean_text(job_desc))
    vectorizer=TfidfVectorizer()
    tfidf_matrix=vectorizer.fit_transform([processed_resume,processed_job_desc])
    score=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]*100
    return round(score,2),processed_resume,processed_job_desc

#Main App

def main():
    upload_pdf=st.file_uploader("Upload your Resume (pdf)",type=['pdf'])
    job_desc=st.text_area("Paste the job description" , height=250)

    if st.button("CHECK"):
        if not upload_pdf:
            st.warning("Please upload your resume")
            return
        if not job_desc:
            st.warning("Please paste the job description")
            return
        

        with st.spinner("Analyzing your resume...."):
            resume_text=extract_text_from_pdf(upload_pdf)
            if not resume_text:
                st.error("COULD NOT EXTRACT TEXT FROM PDF")
                return
            
#calculate similarity
            
            similarity_score,processed_resume,processed_job_desc=cal_sim(resume_text,job_desc)

#result

            st.subheader("Results")
            st.metric("Match Score",f"{similarity_score:.2f}%")
            

            if similarity_score<40:
                st.warning("Low Match, consider tailoring your resume more closely.")
            elif similarity_score<70:
                st.info("Good Match. Your resume aligin fairly well")
            else:
                st.success("Excellent Match ! Your resume strongly aligns.")


if __name__=="__main__":
    main()