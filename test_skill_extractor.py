from skill_extractor import extract_skills_with_llm


resume = """
B.Tech Computer Science student.

Skills:
Python, Java, SQL, Git, HTML, CSS.

Projects:
Built an AI Resume Matcher using Python,
Streamlit and machine learning.
"""


job_description = """
We are looking for a Python developer.

Requirements:

Python
FastAPI
Docker
AWS
REST APIs
PostgreSQL
LangChain
RAG
Git
Machine Learning
"""


result = extract_skills_with_llm(
    resume,
    job_description
)


print("\nRESUME SKILLS:")
for skill in result.resume_skills:
    print("-", skill)


print("\nJOB SKILLS:")
for skill in result.job_skills:
    print("-", skill)