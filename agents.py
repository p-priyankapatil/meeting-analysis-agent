import ollama

class ToneAgent:
    def analyze(self, text):
        prompt = f"""
Analyze the overall tone of this meeting.

{text}

Rules:
- Return ONLY one word
- No explanation

Output:
Tone: Positive OR Negative OR Neutral
"""

        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0}
        )

        return response["message"]["content"]

class RequirementAgent:
    def analyze(self, text):
        prompt = f"""
Extract ONLY business requirements from this meeting.

{text}

Definition:
- Requirement = clear business action or decision

STRICT RULES:
- Do NOT include names of people
- Do NOT describe who said it
- Do NOT include discussion or explanation
- Only include actions that need to be done
- Keep each point short and clear

Ignore:
- Agenda
- Meeting flow
- Conversations

Output format:

Requirements:
- <action>
- <action>
- <action>
"""

        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0}
        )

        return response["message"]["content"]

class SummaryAgent:
    def analyze(self, text):
        prompt = f"""
Summarize this meeting in 2-3 lines:

{text}

Output:
Summary:
<summary>
"""
        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0}
        )
        return response["message"]["content"]