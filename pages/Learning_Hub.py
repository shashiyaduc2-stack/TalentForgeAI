import streamlit as st
from utils.ai_client import ask_ai

st.set_page_config(
    page_title="AI Learning Hub",
    page_icon="📚"
)

st.title("📚 AI Learning Hub")

language = st.selectbox(
    "Select Technology",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL"
    ]
)

TOPICS = {
    "Python": [
        "Introduction",
        "Variables",
        "Data Types",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Functions",
        "OOP",
        "File Handling",
        "Exception Handling"
    ],
    "Java": [
        "Introduction",
        "Variables",
        "Data Types",
        "Operators",
        "Loops",
        "Methods",
        "OOP",
        "Exception Handling"
    ],
    "C": [
        "Introduction",
        "Variables",
        "Data Types",
        "Operators",
        "Loops",
        "Functions",
        "Pointers",
        "Structures"
    ],
    "C++": [
        "Introduction",
        "Variables",
        "OOP",
        "Inheritance",
        "Polymorphism",
        "STL",
        "Vectors"
    ],
    "SQL": [
        "Introduction",
        "Database",
        "Tables",
        "SELECT",
        "WHERE",
        "GROUP BY",
        "JOINS",
        "Subqueries"
    ]
}

topic = st.selectbox(
    "Choose Topic",
    TOPICS[language]
)

st.info(f"{language} → {topic}")

st.subheader("📖 Notes")

if st.button("Generate Notes"):

    with st.spinner("Generating Notes..."):

        prompt = f"""
Explain {topic} in {language}.

Give:
1. Definition
2. Syntax
3. Example
4. Important Points

Keep it beginner friendly.
"""

        notes = ask_ai(prompt)

    st.markdown(notes)

st.divider()

st.subheader("🤖 Ask Doubt")

doubt = st.text_input(
    "Ask your doubt"
)

if st.button("Explain Doubt"):

    if doubt.strip():

        prompt = f"""
You are an expert {language} tutor.

Topic:
{topic}

Student Doubt:
{doubt}

Explain in simple language with examples.
"""

        answer = ask_ai(prompt)

        if "ERROR:" in answer:

            st.error(answer)

        else:

            st.markdown(answer)

    else:

        st.warning("Please enter a doubt.")

st.divider()

st.subheader("Quiz")

if st.button("Generate Quiz"):

    with st.spinner("Generating Quiz..."):

        quiz_prompt = f"""
Create 5 MCQ questions on {topic} in {language}.

Format:

Q1:
A)
B)
C)
D)

Answer:

Q2:
A)
B)
C)
D)

Answer:

Q3:
A)
B)
C)
D)

Answer:

Q4:
A)
B)
C)
D)

Answer:

Q5:
A)
B)
C)
D)

Answer:
"""

        quiz = ask_ai(quiz_prompt)

    st.markdown(quiz)
st.divider()

st.caption(
    "TalentForge AI • Career Intelligence Platform"
)