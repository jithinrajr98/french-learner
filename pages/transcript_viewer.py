from core.transcript import TranscriptManager
import streamlit as st

transcript_manager = TranscriptManager()

def render_transcript():
    st.title("📄 Transcript Viewer")
    st.subheader("📘 English Transcript")
    st.text_area("English Sentences", value="\n".join(transcript_manager.english_sentences), height=250)
    st.subheader("📙 French Transcript")
    st.text_area("French Sentences", value="\n".join(transcript_manager.french_sentences), height=250)