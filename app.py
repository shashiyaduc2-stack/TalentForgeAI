import streamlit as st
from agents.evaluation_agent import evaluate_answer
from agents.recruiter_agent import generate_interview_question
from agents.resume_agent import extract_resume_text
from agents.career_agent import generate_roadmap
from utils.ai_client import analyze_resume

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = ""

if "evaluations" not in st.session_state:
    st.session_state["evaluations"] = []

if "current_question" not in st.session_state:
    st.session_state["current_question"] = None

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="TalentForge AI",
    page_icon="🚀"
)

st.title("🚀 TalentForge AI")
st.write("AI-Powered Career Intelligence Platform")

# ----------------------------
# Career Goal Selection
# ----------------------------

career_goal = st.selectbox(
    "Choose Career Goal",
    [
        "AI Engineer",
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "Software Engineer"
    ]
)

# ----------------------------
# Resume Upload
# ----------------------------

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# ----------------------------
# Resume Analysis Agent
# ----------------------------

if resume:

    with st.spinner("Reading Resume..."):
        resume_text = extract_resume_text(resume)

    st.success("Resume Uploaded Successfully")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

            # Save for other agents
            st.session_state["resume_analysis"] = result

        st.subheader("📄 Resume Analysis")
        st.markdown(result)

# ----------------------------
# Career Strategist Agent
# ----------------------------

if "resume_analysis" in st.session_state:

    if st.button("Generate Career Roadmap"):

        with st.spinner("Generating Roadmap..."):

            roadmap = generate_roadmap(
                st.session_state["resume_analysis"],
                career_goal
            )

        st.subheader("🗺 Career Roadmap")
        st.markdown(roadmap)
# ----------------------------
# AI Recruiter Agent
# ----------------------------

st.header("🎤 AI Recruiter Interview")

if "resume_analysis" in st.session_state:

    if st.button("Start Interview"):

        first_question = generate_interview_question(
            career_goal,
            st.session_state["resume_analysis"],
            "No conversation yet"
        )

        st.session_state["current_question"] = first_question

if st.session_state["current_question"] is not None:

    st.write("### Recruiter Question")

    st.write(
        st.session_state["current_question"]
    )

    answer = st.text_area(
        "Your Answer"
    )

    if st.button("Submit Answer"):

        st.session_state["chat_history"] += f"""

Question:
{st.session_state['current_question']}

Answer:
{answer}
"""

        evaluation = evaluate_answer(
            st.session_state["current_question"],
            answer,
            career_goal
        )

        st.session_state["evaluations"].append(
            evaluation
        )

        next_question = generate_interview_question(
            career_goal,
            st.session_state["resume_analysis"],
            st.session_state["chat_history"]
        )

        st.session_state["current_question"] = next_question

        st.rerun()

# ----------------------------
# Interview Feedback
# ----------------------------

if len(st.session_state["evaluations"]) > 0:

    st.subheader("📊 Interview Feedback")

    st.markdown(
        st.session_state["evaluations"][-1]
    )