from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):

    matching_skills: list[str]

    missing_skills: list[str]
    

    candidate_summary: str

    strengths: list[str]

    weaknesses: list[str]

    candidate_type: str
    
    experience_match: str

    experience_score: float = Field(
        ge=0,
        le=10
    )

    project_match: str

    project_score: float = Field(
        ge=0,
        le=10
    )
    
    education_match: str

    education_score: float = Field(
        ge=0,
        le=10
    )

    suitability_score: float = Field(
        ge=0,
        le=10
    )

    improvement_suggestions: list[str]


class SkillExtraction(BaseModel):

    resume_skills: list[str]

    job_skills: list[str]