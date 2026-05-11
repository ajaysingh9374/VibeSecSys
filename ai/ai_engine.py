import os


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
    return prompt_template
