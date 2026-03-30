from audio_agent import AudioAgent
from agents import ToneAgent, RequirementAgent, SummaryAgent

def main():
    print("Enter audio file path:")
    audio_file = input(">> ")

    audio_agent = AudioAgent()

    tone_agent = ToneAgent()
    req_agent = RequirementAgent()
    summary_agent = SummaryAgent()

    # Step 1: Audio → Text
    text = audio_agent.speech_to_text(audio_file)

    print("\nTranscript:\n")
    print(text)

    # Step 2: Agents
    tone = tone_agent.analyze(text)
    requirements = req_agent.analyze(text)
    summary = summary_agent.analyze(text)

    print("\n=== Final Analysis (Agent Based) ===\n")
    print(tone)
    print(requirements)
    print(summary)


if __name__ == "__main__":
    main()