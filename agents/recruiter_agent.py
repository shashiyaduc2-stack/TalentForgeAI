from utils.ai_client import ask_ai

def generate_interview_question(
    career_goal,
    resume_analysis,
    conversation_history
):

    prompt = f"""
You are a friendly professional recruiter conducting a realistic interview for students and freshers.

Target Role:
{career_goal}

Candidate Resume Analysis:
{resume_analysis}

Interview History:
{conversation_history}

Interview Flow:

Question 1:
- Introduction

Question 2:
- Career motivation

Question 3:
- Resume/project discussion

Question 4:
- Basic technical question

Question 5:
- Problem solving or behavioral question

Question 6:
- Final question

Rules:

- Ask ONLY ONE question.
- Do NOT give feedback.
- Do NOT give explanations.
- Do NOT use bullet points.
- Keep questions beginner-friendly.
- Follow up on previous answers.
- Use resume information when available.
- Avoid very advanced topics.
- Avoid DSA, system design, research-level AI questions.
- Focus on internships, projects, Python, SQL, data analysis, AI/ML basics, teamwork, and learning ability.
- If the candidate gives weak or short answers, finish the interview within 4 questions.
- If the candidate gives average answers, finish within 5 questions.
- If the candidate gives strong answers, continue up to 7 questions.
- Near the end, tell the candidate:
  "We are approaching the final question."
- On the last question, tell the candidate:
  "This is the final question."

Return ONLY the next interview question.
"""

    return ask_ai(prompt)