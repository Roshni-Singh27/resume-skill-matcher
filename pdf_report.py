from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors


def create_pdf_report(
    final_score,
    technical_score,
    experience_score,
    project_score,
    education_score,
    llm_score,
    candidate_type,
    matching_skills,
    missing_skills,
    skill_gap,
    experience_match,
    project_match,
    education_match,
    candidate_summary,
    strengths,
    weaknesses,
    improvement_suggestions
):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    subtitle_style = styles["Heading2"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    elements = []

    # ==========================================
    # TITLE
    # ==========================================

    elements.append(
        Paragraph(
            "AI RESUME SKILL MATCHER",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "Resume Analysis Report",
            subtitle_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # OVERALL SCORE
    # ==========================================

    elements.append(
        Paragraph(
            f"<b>Overall Match Score:</b> "
            f"{final_score}%",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # ==========================================
    # SCORE BREAKDOWN
    # ==========================================

    elements.append(
        Paragraph(
            "Score Breakdown",
            heading_style
        )
    )

    score_data = [
        ["Category", "Score"],
        ["Technical Skills", f"{technical_score}%"],
        ["Experience", f"{experience_score}%"],
        ["Projects", f"{project_score}%"],
        ["Education", f"{education_score}%"],
        ["AI Evaluation", f"{llm_score}%"]
    ]

    score_table = Table(
        score_data,
        colWidths=[
            100 * mm,
            50 * mm
        ]
    )

    score_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 0),
                (-1, -1),
                "CENTER"
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    elements.append(score_table)

    elements.append(
        Spacer(1, 15)
    )

    # ==========================================
    # CANDIDATE PROFILE
    # ==========================================

    elements.append(
        Paragraph(
            "Candidate Profile",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Candidate Type:</b> "
            f"{escape(str(candidate_type))}",
            body_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # MATCHING SKILLS
    # ==========================================

    elements.append(
        Paragraph(
            "Matching Skills",
            heading_style
        )
    )

    if matching_skills:

        for skill in matching_skills:

            elements.append(
                Paragraph(
                    f"&#10003; {escape(str(skill))}",
                    body_style
                )
            )

    else:

        elements.append(
            Paragraph(
                "No matching skills found.",
                body_style
            )
        )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # MISSING SKILLS
    # ==========================================

    elements.append(
        Paragraph(
            "Missing Skills",
            heading_style
        )
    )

    if missing_skills:

        for skill in missing_skills:

            elements.append(
                Paragraph(
                    f"&#10007; {escape(str(skill))}",
                    body_style
                )
            )

    else:

        elements.append(
            Paragraph(
                "No major missing skills.",
                body_style
            )
        )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # SKILL GAP
    # ==========================================

    elements.append(
        Paragraph(
            "Skill Gap Analysis",
            heading_style
        )
    )

    if skill_gap["priority"]:

        for skill in skill_gap["priority"]:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    body_style
                )
            )

    else:

        elements.append(
            Paragraph(
                "No major skill gaps detected.",
                body_style
            )
        )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # EXPERIENCE
    # ==========================================

    elements.append(
        Paragraph(
            "Experience Analysis",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            escape(str(experience_match)),
            body_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Experience Score:</b> "
            f"{experience_score}%",
            body_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # PROJECTS
    # ==========================================

    elements.append(
        Paragraph(
            "Project Relevance",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            escape(str(project_match)),
            body_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Project Score:</b> "
            f"{project_score}%",
            body_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # EDUCATION
    # ==========================================

    elements.append(
        Paragraph(
            "Education Analysis",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            escape(str(education_match)),
            body_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Education Score:</b> "
            f"{education_score}%",
            body_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # SUMMARY
    # ==========================================

    elements.append(
        Paragraph(
            "Candidate Summary",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            escape(str(candidate_summary)),
            body_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # STRENGTHS
    # ==========================================

    elements.append(
        Paragraph(
            "Strengths",
            heading_style
        )
    )

    if strengths:

        for strength in strengths:

            elements.append(
                Paragraph(
                    f"- {escape(str(strength))}",
                    body_style
                )
            )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # WEAKNESSES
    # ==========================================

    elements.append(
        Paragraph(
            "Weaknesses",
            heading_style
        )
    )

    if weaknesses:

        for weakness in weaknesses:

            elements.append(
                Paragraph(
                    f"- {escape(str(weakness))}",
                    body_style
                )
            )

    elements.append(
        Spacer(1, 12)
    )

    # ==========================================
    # IMPROVEMENT SUGGESTIONS
    # ==========================================

    elements.append(
        Paragraph(
            "Improvement Suggestions",
            heading_style
        )
    )

    if improvement_suggestions:

        for suggestion in improvement_suggestions:

            elements.append(
                Paragraph(
                    f"- {escape(str(suggestion))}",
                    body_style
                )
            )

    # ==========================================
    # BUILD PDF
    # ==========================================

    document.build(elements)

    buffer.seek(0)

    return buffer.getvalue()