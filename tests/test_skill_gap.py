from skill_gap import analyze_skill_gap


def test_skill_gap_with_missing_skills():

    missing_skills = [
        "Docker",
        "AWS",
        "FastAPI"
    ]

    result = analyze_skill_gap(
        missing_skills
    )

    assert "priority" in result
    assert "recommendations" in result

    assert len(result["priority"]) > 0
    assert len(result["recommendations"]) > 0


def test_skill_gap_with_no_missing_skills():

    missing_skills = []

    result = analyze_skill_gap(
        missing_skills
    )

    assert result["priority"] == []