from audio_agent import AudioAgent
from agent import AnalysisAgent

def main():
    print("Enter audio file path:")
    audio_file = input(">> ")

    audio_agent = AudioAgent()
    analysis_agent = AnalysisAgent()

    try:
        # Step 1: Audio → Text
        text = audio_agent.speech_to_text(audio_file)

        print("\nTranscript:\n")
        print(text)

        # Step 2: Text → Analysis
        result = analysis_agent.analyze(text)

        print("\n=== Final Analysis ===\n")
        print(result)

    except Exception as e:
        print("\nError:", str(e))


if __name__ == "__main__":
    main()