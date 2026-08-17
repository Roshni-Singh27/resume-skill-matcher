from llm import analyze_resume


resume = """
Riya Sharma

B.Tech Computer Science student.

Skills:
Python
SQL
Git
Machine Learning

Projects:
Built a machine learning project using Python.
Created a Streamlit resume analysis application.

No professional work experience.
"""


job_description = """
We are looking for a Machine Learning Engineer.

Requirements:

Python
SQL
Machine Learning
Git

Experience:
2+ years of professional experience
working with machine learning systems.

Experience with:
Docker
AWS
REST APIs
"""


result = analyze_resume(
    resume,
    job_description
)


print("\n" + "=" * 50)
print("EXPERIENCE MATCH")
print("=" * 50)

print(result.experience_match)


print("\n" + "=" * 50)
print("EXPERIENCE SCORE")
print("=" * 50)

print(f"{result.experience_score}/10")


print("\n" + "=" * 50)
print("EDUCATION MATCH")
print("=" * 50)

print(result.education_match)


print("\n" + "=" * 50)
print("EDUCATION SCORE")
print("=" * 50)

print(f"{result.education_score}/10")

print("\n" + "=" * 50)
print("PROJECT MATCH")
print("=" * 50)

print(result.project_match)


print("\n" + "=" * 50)
print("PROJECT SCORE")
print("=" * 50)

print(f"{result.project_score}/10")


print("\n" + "=" * 50)
print("OVERALL SUITABILITY")
print("=" * 50)

print(f"{result.suitability_score}/10")