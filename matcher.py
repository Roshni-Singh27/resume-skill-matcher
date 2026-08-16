import re


# Common technical skills
SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node.js",
    "express",
    "django",
    "flask",
    "spring",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "numpy",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "opencv",
    "rest api",
    "graphql",
    "linux",
    "jenkins",
    "terraform",
    "spark",
    "hadoop",
    "tableau",
    "power bi",
}


def normalize_text(text):
    """
    Convert text to lowercase and remove
    unnecessary special characters.
    """

    text = text.lower()

    text = text.replace("nodejs", "node.js")
    text = text.replace("scikit learn", "scikit-learn")
    text = text.replace("restful api", "rest api")

    return text


def extract_skills(text):
    """
    Extract known technical skills from text.
    """

    text = normalize_text(text)

    found_skills = set()

    for skill in SKILLS:

        # Escape skill name for regex
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.add(skill)

    return sorted(found_skills)


def calculate_match(resume_skills, job_skills):
    """
    Calculate percentage of required job skills
    present in the resume.
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    if not job_set:

        return 0

    matching = resume_set.intersection(job_set)

    missing = job_set - resume_set

    score = (
        len(matching) / len(job_set)
    ) * 100

    return {
        "matching_skills": sorted(matching),
        "missing_skills": sorted(missing),
        "score": round(score, 2)
    }