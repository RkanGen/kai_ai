from groq import Groq
import os
import datetime

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_resume(resume, job_description):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": f"Build a custom resume for this job posting here is the resume: {resume} and here is the job description {job_description}"
            },
            {
                "role": "assistant",
                "content": "Please provide the job posting details, and I'll create a custom resume tailored to the job requirements.\n\nPlease provide the following information:\n\n1. Job title\n2. Job description\n3. Requirements (e.g., skills, experience, education)\n4. Any specific keywords or phrases mentioned in the job posting\n\nOnce I have this information, I'll create a custom resume that highlights your relevant skills and experiences, increasing your chances of getting noticed by the hiring manager."
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content