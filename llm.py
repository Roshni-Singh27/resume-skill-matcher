import ollama

from models import ResumeAnalysis


MODEL_NAME = "llama3.2:3b"


def analyze_resume(
    resume,
    job_description
):

    prompt = f"""
You are a resume screening assistant.

Analyze the candidate resume against the job description.

IMPORTANT:
Return ONLY the requested structured information.
Do not explain your reasoning.
Do not include JSON syntax manually.
Do not include field names inside other fields.
Do not repeat the entire answer inside experience_match
or project_match.

CANDIDATE RESUME:
-----------------
{resume}

JOB DESCRIPTION:
----------------
{job_description}


FIELD INSTRUCTIONS:

matching_skills:
List only technical skills that are present
in both the resume and job description.

missing_skills:
List only important technical skills required
by the job but absent from the resume.

candidate_summary:
Write 2-3 sentences summarizing the candidate.

strengths:
List 3 or fewer important candidate strengths.

weaknesses:
List 3 or fewer important weaknesses.

candidate_type:
Classify the candidate as exactly one of:

Fresher
Entry-Level
Experienced

Use Fresher when there is no professional
work experience.

Use Entry-Level when the candidate has
limited professional experience.

Use Experienced when the candidate has
substantial professional experience.


experience_match:
Write ONLY 1-2 short sentences comparing
the candidate's experience with the job's
experience requirements.

experience_score:
Give a number from 0 to 10.
0 means no relevant experience.
10 means the candidate fully meets the
experience requirements.

EDUCATION ANALYSIS:

education_match:
Write ONLY 1-2 short sentences comparing
the candidate's education with the job's
education requirements.

education_score:
Give a number from 0 to 10.

10 means the candidate fully meets the
education requirements.

5 means the education is somewhat relevant.

0 means the candidate does not meet the
education requirements.

Do not invent degrees or qualifications.


PROJECT ANALYSIS:

project_match:
Write ONLY 1-2 short sentences comparing
the candidate's projects with the job.

project_score:
Give a number from 0 to 10 based on project
relevance.

Do not invent projects.
If no projects are mentioned, clearly state that.


suitability_score:
Give an overall score from 0 to 10 based on:

- technical skills
- professional experience
- projects
- education
- overall job fit

improvement_suggestions:
List 3-5 specific suggestions for improving
the candidate's suitability.

IMPORTANT:
Do not put explanations, scores, or suggestions
inside experience_match.

Do not put explanations, scores, or suggestions
inside project_match.
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
            "temperature": 0,
            "num_ctx": 2048
        }
    )

    result = ResumeAnalysis.model_validate_json(
        response.message.content
    )

    return result