import ollama

class AnalysisAgent:

    def analyze(self, text):
        prompt = f"""
You are an AI meeting analyzer.

Analyze the transcript below.

---------------------
TRANSCRIPT:
{text}
---------------------

DEFINITION:
- "Requirement" means an ACTION or DECISION agreed or suggested in the meeting.
- Do NOT include general discussion or background.
- Only include actionable points (things to be done).

STRICT RULES:
- Follow exact format
- Do not add extra headings
- Do not explain anything

---------------------
OUTPUT FORMAT:

Tone: <Positive/Negative/Neutral>

Requirements means:
- A clear ACTION to be taken
- Do NOT include names of people
- Do NOT describe who said it
- Focus only on WHAT needs to be done

Summary:
<2-3 line summary>
---------------------
"""

        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0}
        )

        return response["message"]["content"]