import ollama

from models import ResumeAnalysis


MODEL_NAME = "llama3.2:3b"


def analyze_resume(resume, job_description):

    prompt = f"""
You are an expert technical recruiter.

Compare the candidate resume with the job description.

IMPORTANT RULES:

1. Only identify skills that are actually present in the resume.
2. Do not invent candidate experience.
3. Identify skills required by the job description but missing from the resume.
4. Give a suitability score from 0 to 10.
5. Give practical improvement suggestions.
6. Return the result according to the provided JSON schema.

CANDIDATE RESUME:
-----------------
{resume}

JOB DESCRIPTION:
----------------
{job_description}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format=ResumeAnalysis.model_json_schema(),
        options={
            "temperature": 0
        }
    )

    result = ResumeAnalysis.model_validate_json(
        response.message.content
    )

    return result