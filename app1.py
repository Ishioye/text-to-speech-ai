import streamlit as st
from TTS.api import TTS
import os

st.title("🧠 Text to Speech AI System")

st.write("Enter text below and convert it into natural speech.")

# Load model (cached for performance)
@st.cache_resource
def load_model():
    return TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

tts = load_model()

text = st.text_area("Enter Text")

if st.button("Generate Speech"):
    if text.strip() != "":
        output_path = "outputs/generated_audio.wav"
        os.makedirs("outputs", exist_ok=True)

        tts.tts_to_file(text=text, file_path=output_path)

        st.success("Audio Generated!")

        st.audio(output_path)
    else:
        st.warning("Please enter some text.")