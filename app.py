import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from llm import analyze_resume
from skill_gap import analyze_skill_gap
from matcher import calculate_match
from pdf_report import create_pdf_report

from skill_extractor import (
    extract_skills_with_llm
)


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
                # Intelligent LLM-based skill extraction

                skill_result = extract_skills_with_llm(
                    resume_text,
                    job_description
                )

                resume_skills = skill_result.resume_skills

                job_skills = skill_result.job_skills


                # Deterministic skill matching

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

                experience_score = (
                    result.experience_score * 10
                )

                project_score = (
                    result.project_score * 10
                )

                education_score = (
                    result.education_score * 10
                )

                llm_score = (
                    result.suitability_score * 10
                )


                final_score = (
                    technical_score * 0.45
                    +
                    experience_score * 0.20
                    +
                    project_score * 0.15
                    +
                    education_score * 0.10
                    +
                    llm_score * 0.10
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

            col1, col2, col3, col4, col5 = st.columns(5)


            with col1:

                st.metric(
                    "Final Match",
                    f"{final_score}%"
                )


            with col2:

                st.metric(
                    "Technical Skills",
                    f"{technical_score}%"
                )


            with col3:

                st.metric(
                    "Experience",
                    f"{experience_score}%"
                )


            with col4:

                st.metric(
                    "Projects",
                    f"{project_score}%"
                )


            with col5:

                st.metric(
                    "Education",
                    f"{education_score}%"
                )

            st.metric(
                "🤖 AI Evaluation",
                    f"{result.suitability_score}/10"
            )
            st.progress(
                int(final_score)
            )
            
            # ==========================================
            # CANDIDATE EVALUATION CHART
            # ==========================================

            st.subheader(
                "📊 Candidate Evaluation"
            )

            chart_data = {
                "Category": [
                    "Technical Skills",
                    "Experience",
                    "Projects",
                    "Education",
                    "AI Evaluation"
                ],

                "Score": [
                    technical_score,
                    experience_score,
                    project_score,
                    education_score,
                    llm_score
                ]
            }

            df = pd.DataFrame(chart_data)

            st.bar_chart(
                df.set_index("Category")
            )
            
            
            st.subheader(
                "👤 Candidate Profile"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Candidate Type",
                    result.candidate_type
                )

            with col2:

                st.metric(
                    "Experience",
                    f"{experience_score}%"
                )

            with col3:

                st.metric(
                    "Education",
                    f"{education_score}%"
                )
                
            # ==========================================
            # DOWNLOADABLE ANALYSIS REPORT
            # ==========================================

            report = f"""
            AI RESUME SKILL MATCHER
            =======================

            RESUME ANALYSIS REPORT


            OVERALL MATCH
            -------------
            Final Match Score: {final_score}%


            SCORE BREAKDOWN
            ---------------

            Technical Skills: {technical_score}%
            Experience: {experience_score}%
            Projects: {project_score}%
            Education: {education_score}%
            AI Evaluation: {result.suitability_score}/10


            CANDIDATE PROFILE
            -----------------

            Candidate Type:
            {result.candidate_type}


            MATCHING SKILLS
            ---------------

            """

            for skill in match_result["matching_skills"]:

                report += f"✓ {skill}\n"


            report += """

            MISSING SKILLS
            --------------

            """

            for skill in match_result["missing_skills"]:

                report += f"✗ {skill}\n"


            report += """

            SKILL GAP ANALYSIS
            ------------------

            Priority Skills:
            """

            if skill_gap["priority"]:

                for skill in skill_gap["priority"]:

                    report += f"- {skill}\n"

            else:

                report += "No major skill gaps detected.\n"


            report += """

            RECOMMENDED ACTIONS
            -------------------

            """

            if skill_gap["recommendations"]:

                for recommendation in skill_gap["recommendations"]:

                    report += f"- {recommendation}\n"

            else:

                report += "No recommendations available.\n"


            report += f"""
            

            EXPERIENCE ANALYSIS
            -------------------

            {result.experience_match}

            Experience Score:
            {experience_score}%


            PROJECT RELEVANCE
            -----------------

            {result.project_match}

            Project Score:
            {project_score}%


            EDUCATION ANALYSIS
            ------------------

            {result.education_match}

            Education Score:
            {education_score}%


            CANDIDATE SUMMARY
            -----------------

            {result.candidate_summary}


            STRENGTHS
            ---------

            """

            for strength in result.strengths:

                report += f"- {strength}\n"


            report += """

            WEAKNESSES
            ----------

            """

            for weakness in result.weaknesses:

                report += f"- {weakness}\n"


            report += """

            IMPROVEMENT SUGGESTIONS
            -----------------------

            """

            for suggestion in result.improvement_suggestions:

                report += f"- {suggestion}\n"
                
            # ==========================================
            # DOWNLOAD REPORT
            # ==========================================

            st.divider()

            st.subheader(
                "📥 Download Report"
            )
                
            st.download_button(
                label="📥 Download Analysis Report",
                data=report,
                file_name="resume_analysis_report.txt",
                mime="text/plain"
            )
            
            # ==========================================
            # PDF REPORT
            # ==========================================

            pdf_data = create_pdf_report(
                final_score=final_score,
                technical_score=technical_score,
                experience_score=experience_score,
                project_score=project_score,
                education_score=education_score,
                llm_score=llm_score,
                candidate_type=result.candidate_type,
                matching_skills=match_result["matching_skills"],
                missing_skills=match_result["missing_skills"],
                skill_gap=skill_gap,
                experience_match=result.experience_match,
                project_match=result.project_match,
                education_match=result.education_match,
                candidate_summary=result.candidate_summary,
                strengths=result.strengths,
                weaknesses=result.weaknesses,
                improvement_suggestions=result.improvement_suggestions
            )


            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_data,
                file_name="resume_analysis_report.pdf",
                mime="application/pdf"
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
            else:

                st.success(
                    "No additional recommendations."
                )
                    

            st.divider()


            # ==========================================
            # EXPERIENCE ANALYSIS
            # ==========================================

            st.subheader(
                "💼 Experience Analysis"
            )

            st.write(
                result.experience_match
            )

            st.progress(
                int(experience_score)
            )


            # ==========================================
            # PROJECT RELEVANCE
            # ==========================================

            st.subheader(
                "🚀 Project Relevance"
            )

            st.write(
                result.project_match
            )

            st.progress(
                int(project_score)
            )
            
            
            st.subheader(
                "🎓 Education Analysis"
            )

            st.write(
                result.education_match
            )

            st.progress(
                int(education_score)
            )


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