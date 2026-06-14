from utils.ai_client import ask_ai

def generate_roadmap(resume_analysis, career_goal):

    prompt = f"""
You are an expert career mentor.

Candidate Analysis:

{resume_analysis}

Target Career:

{career_goal}

Create:

1. Skill Gap Analysis
2. 3 Month Learning Roadmap
3. Recommended Projects
4. Internship Preparation Plan
5. Certifications to Consider

Make the roadmap practical and personalized.
"""

    return ask_ai(prompt)