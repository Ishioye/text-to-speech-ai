import streamlit as st
from TTS.api import TTS
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Text to Speech",
    page_icon="🔊",
    layout="centered"
)

# ---------------- SIMPLE MOBILE UI ----------------
st.markdown("""
<style>
.main {
    padding: 1rem;
}

button {
    width: 100%;
    height: 3em;
    font-size: 18px !important;
}

audio {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🔊 AI Text-to-Speech")

st.write("Convert text into speech using AI.")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

tts = load_model()

# ---------------- INPUT ----------------
text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type something..."
)

os.makedirs("outputs", exist_ok=True)

# ---------------- GENERATE ----------------
if st.button("🎤 Generate Speech"):

    if text.strip():

        output_path = "outputs/speech.wav"

        with st.spinner("Generating speech..."):

            tts.tts_to_file(
                text=text,
                file_path=output_path
            )

        st.success("Audio generated!")

        st.audio(output_path)

        with open(output_path, "rb") as f:
            st.download_button(
                "⬇ Download Audio",
                f,
                file_name="speech.wav"
            )

    else:
        st.warning("Please enter text.")