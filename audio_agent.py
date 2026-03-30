import whisper
import os

class AudioAgent:
    """Handles audio to text conversion"""

    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model("base")
        print("✓ Model loaded")

    def speech_to_text(self, audio_path):
        """
        Convert audio file to text
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"File not found: {audio_path}")

        print(f"Processing audio: {audio_path}")
        print("Starting transcription...")

        result = self.model.transcribe(audio_path)
        text = result["text"]

        print("✓ Transcription done")

        return text