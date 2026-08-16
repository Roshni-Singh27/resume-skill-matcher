from llm import analyze_resume


resume = """
John Doe

Skills:
Python
Java
SQL
Git
HTML
CSS

Education:
B.Tech Computer Science

Projects:
AI Resume Matcher using Python and Streamlit.
"""


job_description = """
We are looking for a Python Developer.

Requirements:

Python
SQL
Docker
AWS
Git
REST APIs
Machine Learning
"""


result = analyze_resume(
    resume,
    job_description
)


print("\nMATCHING SKILLS:")
print(result.matching_skills)

print("\nMISSING SKILLS:")
print(result.missing_skills)

print("\nSUMMARY:")
print(result.candidate_summary)

print("\nSTRENGTHS:")
print(result.strengths)

print("\nWEAKNESSES:")
print(result.weaknesses)

print("\nSCORE:")
print(result.suitability_score)

print("\nSUGGESTIONS:")
print(result.improvement_suggestions)