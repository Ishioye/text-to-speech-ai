import streamlit as st
import requests

st.title("🔊 AI Text to Speech (Cloud Stable)")

text = st.text_area("Enter text")

if st.button("Generate Speech"):
    if text.strip():

        audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={text}&tl=en"

        st.audio(audio_url)

    else:
        st.warning("Enter text first")
