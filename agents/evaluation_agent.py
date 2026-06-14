from utils.ai_client import ask_ai

def evaluate_answer(
    question,
    answer,
    career_goal
):

    prompt = f"""
You are an expert interviewer.

Role:
{career_goal}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate:

1. Communication Score (0-10)
2. Technical Score (0-10)
3. Confidence Score (0-10)
4. Strengths
5. Improvements

Keep the response concise.
"""

    return ask_ai(prompt)