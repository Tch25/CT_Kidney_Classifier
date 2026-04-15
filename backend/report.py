import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# ── Setup Groq ────────────────────────────────────────────────────────────────
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ── Generate Report ───────────────────────────────────────────────────────────
def generate_report(prediction: str, confidence: float) -> str:
    prompt = f"""
    You are a medical imaging assistant. Based on the following CT kidney scan analysis,
    write a short and clear clinical report in 3-4 sentences.

    Findings:
    - Detected condition: {prediction}
    - Confidence score: {confidence * 100:.1f}%


    Important: Do not give a final diagnosis.
    Just describe the findings and suggest consulting a doctor.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
