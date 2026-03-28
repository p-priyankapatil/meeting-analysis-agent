import ollama
def analyze_meeting(meeting_text):
    prompt = f"""
    You are a strict meeting analysis system.

    Your job is to analyze meeting transcripts and ALWAYS provide an answer.

    Do NOT refuse.
    Do NOT say you cannot analyze.
    Do NOT mention privacy or safety.

    Analyze the transcript below:

    {meeting_text}

    Return ONLY this format:

    Tone: <positive/negative/neutral>

    Requirements:
    - <point 1>
    - <point 2>

    Summary:
    <short summary>
    """
    response = ollama.chat(
    model='llama3.2:1b',
    messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


meeting_text = """
Meeting was about discussing project timelines and next steps.
"""

result = analyze_meeting(meeting_text)

print("\n=== Meeting Analysis ===\n")
print(result)