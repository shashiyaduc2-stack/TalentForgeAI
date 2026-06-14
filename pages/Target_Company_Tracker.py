import streamlit as st
from utils.ai_client import ask_ai

st.set_page_config(
    page_title="Target Company Tracker"
    
)

st.title(" Target Company Tracker")

companies = [
    "Google",
    "Microsoft",
    "Amazon",
    "Meta",
    "Adobe",
    "NVIDIA",
    "Oracle",
    "Infosys",
    "TCS",
    "Wipro"
]

company = st.selectbox(
    "Select Target Company",
    companies
)

if "resume_analysis" not in st.session_state:

    st.warning(
        "Please analyze your resume first from the main page."
    )

else:

    if st.button("Check Company Match"):

        with st.spinner(
            "Analyzing your profile..."
        ):

            prompt = f"""
You are an expert recruiter.

Resume Analysis:

{st.session_state['resume_analysis']}

Evaluate the candidate for {company}.

Provide:

# Match Score (/100)

# Strengths

# Missing Skills

# Recommended Learning Path

# Interview Preparation Tips

Keep response concise and professional.
"""

            result = ask_ai(prompt)

        st.markdown(result)
st.divider()

st.caption(
    "TalentForge AI • Career Intelligence Platform"
)