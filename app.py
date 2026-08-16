import streamlit as st

from resume_parser import extract_resume_text
from llm import analyze_resume
from matcher import extract_skills, calculate_match
from skill_gap import analyze_skill_gap


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Skill Matcher",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📄 AI-Powered Resume Skill Matcher")

st.write(
    "Analyze your resume against a job description "
    "using a locally running LLM."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("📄 Resume")

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "txt"]
    )


with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )


st.divider()


# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button(
    "🚀 Analyze Resume",
    type="primary"
):

    # ----------------------------------------------
    # INPUT VALIDATION
    # ----------------------------------------------

    if resume_file is None:

        st.error(
            "Please upload a resume."
        )

    elif not job_description.strip():

        st.error(
            "Please enter a job description."
        )

    else:

        try:

            # ------------------------------------------
            # ANALYSIS
            # ------------------------------------------

            with st.spinner(
                "AI is analyzing your resume..."
            ):

                # Extract resume text
                resume_text = extract_resume_text(
                    resume_file
                )

                # LLM analysis
                result = analyze_resume(
                    resume_text,
                    job_description
                )

                # Extract skills
                resume_skills = extract_skills(
                    resume_text
                )

                job_skills = extract_skills(
                    job_description
                )

                # Calculate skill match
                match_result = calculate_match(
                    resume_skills,
                    job_skills
                )

                # Analyze skill gaps
                skill_gap = analyze_skill_gap(
                    match_result["missing_skills"]
                )

                # --------------------------------------
                # CALCULATE FINAL SCORE
                # --------------------------------------

                technical_score = match_result["score"]

                llm_score = (
                    result.suitability_score * 10
                )

                final_score = (
                    technical_score * 0.70
                    +
                    llm_score * 0.30
                )

                final_score = round(
                    final_score,
                    2
                )

            # ------------------------------------------
            # SUCCESS MESSAGE
            # ------------------------------------------

            st.success(
                "Analysis completed successfully!"
            )


            # ==========================================
            # SCORE SECTION
            # ==========================================

            st.subheader(
                "🎯 Resume Match Score"
            )

            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    "Final Match",
                    f"{final_score}%"
                )


            with col2:

                st.metric(
                    "Technical Skill Match",
                    f"{technical_score}%"
                )


            with col3:

                st.metric(
                    "AI Evaluation",
                    f"{result.suitability_score}/10"
                )


            st.progress(
                int(final_score)
            )


            # ------------------------------------------
            # SCORE INTERPRETATION
            # ------------------------------------------

            if final_score >= 80:

                st.success(
                    "Excellent match! The candidate "
                    "closely matches the job requirements."
                )

            elif final_score >= 65:

                st.info(
                    "Good match! The candidate meets "
                    "many of the important requirements."
                )

            elif final_score >= 50:

                st.warning(
                    "Moderate match. Several important "
                    "skills are missing."
                )

            else:

                st.error(
                    "Low match. Significant skill gaps "
                    "exist for this position."
                )


            st.divider()


            # ==========================================
            # SKILLS SECTION
            # ==========================================

            col1, col2 = st.columns(2)


            # ------------------------------------------
            # MATCHING SKILLS
            # ------------------------------------------

            with col1:

                st.subheader(
                    "✅ Matching Skills"
                )

                if match_result["matching_skills"]:

                    for skill in match_result[
                        "matching_skills"
                    ]:

                        st.success(
                            skill
                        )

                else:

                    st.warning(
                        "No matching skills found."
                    )


            # ------------------------------------------
            # MISSING SKILLS
            # ------------------------------------------

            with col2:

                st.subheader(
                    "❌ Missing Skills"
                )

                if match_result["missing_skills"]:

                    for skill in match_result[
                        "missing_skills"
                    ]:

                        st.error(
                            skill
                        )

                else:

                    st.success(
                        "No major missing skills!"
                    )


            st.divider()


            # ==========================================
            # SKILL COVERAGE
            # ==========================================

            st.subheader(
                "📚 Skill Coverage"
            )


            if job_skills:

                for skill in job_skills:

                    if skill in resume_skills:

                        st.success(
                            f"✓ {skill}"
                        )

                    else:

                        st.error(
                            f"✗ {skill}"
                        )

            else:

                st.warning(
                    "No recognized technical skills "
                    "were found in the job description."
                )


            st.divider()


            # ==========================================
            # SKILL GAP ANALYSIS
            # ==========================================

            st.subheader(
                "🎯 Skill Gap Analysis"
            )


            if skill_gap["priority"]:

                st.write(
                    "Skills you should prioritize:"
                )

                for skill in skill_gap[
                    "priority"
                ]:

                    st.warning(
                        f"Learn: {skill}"
                    )

            else:

                st.success(
                    "No major skill gaps detected!"
                )


            # ==========================================
            # RECOMMENDED ACTIONS
            # ==========================================

            st.subheader(
                "🚀 Recommended Actions"
            )


            if skill_gap["recommendations"]:

                for recommendation in skill_gap[
                    "recommendations"
                ]:

                    st.info(
                        recommendation
                    )


            st.divider()


            # ==========================================
            # CANDIDATE SUMMARY
            # ==========================================

            st.subheader(
                "👤 Candidate Summary"
            )

            st.write(
                result.candidate_summary
            )


            st.divider()


            # ==========================================
            # STRENGTHS
            # ==========================================

            st.subheader(
                "💪 Strengths"
            )


            if result.strengths:

                for strength in result.strengths:

                    st.write(
                        f"• {strength}"
                    )


            st.divider()


            # ==========================================
            # WEAKNESSES
            # ==========================================

            st.subheader(
                "⚠️ Weaknesses"
            )


            if result.weaknesses:

                for weakness in result.weaknesses:

                    st.write(
                        f"• {weakness}"
                    )


            st.divider()


            # ==========================================
            # IMPROVEMENT SUGGESTIONS
            # ==========================================

            st.subheader(
                "💡 Improvement Suggestions"
            )


            if result.improvement_suggestions:

                for suggestion in result.improvement_suggestions:

                    st.info(
                        suggestion
                    )


        except Exception as e:

            st.error(
                f"Analysis failed: {e}"
            )