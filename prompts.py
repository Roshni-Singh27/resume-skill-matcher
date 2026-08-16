SYSTEM_PROMPT = """
You are an expert technical recruiter and resume analyst.

Your job is to compare a candidate's resume with a job description.

Analyze:
1. Matching skills
2. Missing skills
3. Candidate strengths
4. Candidate weaknesses
5. Overall suitability
6. Improvement suggestions

Be factual and do not invent experience that is not present in the resume.
"""


def create_matching_prompt(resume, job_description):

    return f"""
{SYSTEM_PROMPT}

CANDIDATE RESUME:
-----------------
{resume}

JOB DESCRIPTION:
----------------
{job_description}

Analyze the candidate against the job description.

Return your answer in this format:

MATCHING SKILLS:
- skill 1
- skill 2

MISSING SKILLS:
- skill 1
- skill 2

CANDIDATE SUMMARY:
Write a short summary.

STRENGTHS:
- strength 1
- strength 2

WEAKNESSES:
- weakness 1
- weakness 2

SUITABILITY SCORE:
Give a score from 0 to 10.

IMPROVEMENT SUGGESTIONS:
- suggestion 1
- suggestion 2
- suggestion 3
"""