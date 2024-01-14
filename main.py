import streamlit as st
from app import download_youtube_audio
from app import transcriber

st.set_page_config("Youtube Video Transcriber",page_icon="🎤")

st.title("Youtube Video Transcriber 🎤")

url = st.text_input("Enter Youtube Video URL")

if st.button("Transcribe"):
    with st.spinner("Downloading Audio Please wait..."):
        file_path = download_youtube_audio(url)
        st.success("Audio Downloaded")
    
    with st.spinner("Transcribing Audio Please wait..."):

        Transcript = transcriber(file_path)

        st.success("Transcription Complete")
        
        with st.expander("See Transcript"):
            st.write(Transcript)