from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from resume_generator import generate_resume

app = FastAPI()

class ResumeRequest(BaseModel):
    resume: str
    job_description: str

@app.post("/generate-resume")
async def create_resume(request: ResumeRequest):
    try:
        generated_resume = generate_resume(request.resume, request.job_description)
        return {"resume": generated_resume}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))