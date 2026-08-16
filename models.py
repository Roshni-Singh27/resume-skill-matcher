from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):

    matching_skills: list[str]

    missing_skills: list[str]

    candidate_summary: str

    strengths: list[str]

    weaknesses: list[str]

    suitability_score: float = Field(
        ge=0,
        le=10
    )

    improvement_suggestions: list[str]