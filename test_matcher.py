from matcher import extract_skills, calculate_match


resume = """
I am a Python developer with experience in SQL,
Git, Java and HTML.
"""


job = """
We are looking for a Python developer with
SQL, Git, Docker, AWS and REST API experience.
"""


resume_skills = extract_skills(resume)

job_skills = extract_skills(job)


print("Resume Skills:")
print(resume_skills)


print("\nJob Skills:")
print(job_skills)


result = calculate_match(
    resume_skills,
    job_skills
)


print("\nMatching Skills:")
print(result["matching_skills"])


print("\nMissing Skills:")
print(result["missing_skills"])


print("\nScore:")
print(result["score"])