from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

tts.tts_to_file(
    text="Hello Deborah, your text to speech model is working perfectly.",
    file_path="output.wav"
)