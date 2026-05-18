from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

tts.tts_to_file(
    text="Hello, this is a clean test",
    file_path="test.wav"
)