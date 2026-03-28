import ollama

def analyze_meeting(meeting_text):
    prompt = f"""
Analyze the transcript:

{meeting_text}

Strict Rules:
- Do not add explanations.
- Do not add extra text.
- Follow Exact format only.

Give output:
Tone: <Positive/Negative/Neutral>

Requirements:

- <point 1>
- <point 2>

Summary:
"""

    response = ollama.chat(
        model='llama3.2:1b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


def get_user_input():
    print("\nEnter meeting transcript (type 'exit' to quit):")
    return input(">> ")


def display_output(result):
    print("\n=== Meeting Analysis ===\n")
    print(result)


def main():
    print("Program started...")

    while True:
        meeting_text = get_user_input()

        if meeting_text.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        result = analyze_meeting(meeting_text)
        display_output(result)


if __name__ == "__main__":
    main()