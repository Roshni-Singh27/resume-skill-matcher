import ollama

from models import SkillExtraction


MODEL_NAME = "llama3.2:3b"


def extract_skills_with_llm(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert technical recruiter.

Extract technical and professional skills explicitly
mentioned in the resume and job description.

IMPORTANT RULES:

1. Only extract skills explicitly mentioned in the text.
2. Do not invent skills.
3. Do not infer skills from job titles.
4. Include programming languages.
5. Include frameworks and libraries.
6. Include databases.
7. Include cloud technologies.
8. Include developer tools.
9. Include AI/ML technologies.
10. Include relevant technical concepts.
11. Keep each skill as a short standardized name.
12. Avoid duplicate skills.

Examples:

"Amazon Web Services" → "AWS"
"RESTful APIs" → "REST API"
"Scikit Learn" → "scikit-learn"
"Node JS" → "Node.js"

CANDIDATE RESUME:
-----------------
{resume_text}

JOB DESCRIPTION:
----------------
{job_description}

Return the skills separately for the resume and
job description.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format=SkillExtraction.model_json_schema(),
        options={
            "temperature": 0
        }
    )

    result = SkillExtraction.model_validate_json(
        response.message.content
    )

    return result