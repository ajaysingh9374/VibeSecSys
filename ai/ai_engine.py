import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_ai_analysis(ai_input: str):
    print("AI module initialized")
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("API key loaded successfully")
    else:
        print("Error: OPENAI_API_KEY not found")

    prompt_template = f"""You are a cybersecurity analyst.
Analyze the following scan results and provide:
-Summary of findings
-Identified risks
-Misconfigurations
-Recommendations

Scan Data:
{ai_input}
"""

    print("AI prompt prepared")
    print("Sending data to AI...")

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt_template,
        )
    except Exception:
        print("AI request failed")
        return "AI request failed"

    print("AI response received")
    return response.output_text
