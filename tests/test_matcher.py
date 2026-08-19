from matcher import calculate_match


def test_matching_skills():

    resume_skills = [
        "Python",
        "SQL",
        "Git"
    ]

    job_skills = [
        "Python",
        "SQL",
        "Docker"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert "python" in [
        skill.lower()
        for skill in result["matching_skills"]
    ]

    assert "sql" in [
        skill.lower()
        for skill in result["matching_skills"]
    ]


def test_missing_skills():

    resume_skills = [
        "Python",
        "SQL"
    ]

    job_skills = [
        "Python",
        "SQL",
        "Docker"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert "docker" in [
    skill.lower()
    for skill in result["missing_skills"]
]


def test_perfect_match():

    resume_skills = [
        "Python",
        "SQL",
        "Git"
    ]

    job_skills = [
        "Python",
        "SQL",
        "Git"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert result["score"] == 100


def test_no_match():

    resume_skills = [
        "Python"
    ]

    job_skills = [
        "Java"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert result["score"] == 0
    
def test_empty_resume_skills():

    resume_skills = []

    job_skills = [
        "Python",
        "SQL"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert result["score"] == 0
    assert result["matching_skills"] == []


def test_empty_job_skills():

    resume_skills = [
        "Python",
        "SQL"
    ]

    job_skills = []

    result = calculate_match(
        resume_skills,
        job_skills
    )

    assert result["score"] == 0
    assert result["missing_skills"] == []


def test_case_insensitive_matching():

    resume_skills = [
        "Python",
        "SQL"
    ]

    job_skills = [
        "python",
        "sql"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    matching_skills = [
        skill.lower()
        for skill in result["matching_skills"]
    ]

    assert "python" in matching_skills
    assert "sql" in matching_skills