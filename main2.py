import ollama

def analyze_meeting(meeting_text):
    prompt = """
    You are a meeting analysis system
    analyze the transcript below:

    {meeting_text}

    IMPORTANT:
    - Return ONLY the answer
    - Do NOT explain anything

    Output format:
    
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