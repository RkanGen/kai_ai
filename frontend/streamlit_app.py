import streamlit as st
import requests

API_URL = "http://backend:8000/generate-resume"

st.title("Resume Builder Chatbot")

resume = st.text_area("Paste your current resume here:")
job_description = st.text_area("Paste the job description here:")

if st.button("Generate Custom Resume"):
    if resume and job_description:
        with st.spinner("Generating custom resume..."):
            response = requests.post(API_URL, json={"resume": resume, "job_description": job_description})
            if response.status_code == 200:
                generated_resume = response.json()["resume"]
                st.success("Custom resume generated successfully!")
                st.markdown(generated_resume)
            else:
                st.error("An error occurred while generating the resume.")
    else:
        st.warning("Please provide both your resume and the job description.")