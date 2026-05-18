import streamlit as st

st.title("🔊 Text to Speech (Cloud Version)")

text = st.text_area("Enter text")

if st.button("Generate Speech"):
    if text.strip():
        st.success("Cloud deployment successful!")

        st.audio(
            f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={text}&tl=en"
        )
    else:
        st.warning("Please enter text")
