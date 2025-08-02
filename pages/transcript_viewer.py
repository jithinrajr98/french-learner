from core.transcript import TranscriptManager
import streamlit as st
from config.settings import TRANSCRIPT_YOUTUBE
from core.llm_utils import LLMUtils

llm_utils = LLMUtils()
transcript_manager = TranscriptManager()

def render_transcript():
    st.title("📄 YouTube Transcript Extractor")
    st.header("🎥 Video Input")
    
    video_id = st.text_input("Enter YouTube Video ID:", placeholder="e.g., gUdkxWNJTr0")
    if video_id:
        try:
            transcript_manager.extract_transcript(video_id)
            st.success("Transcript extracted successfully!")
        except Exception as e:
            st.error(f"Error extracting transcript: {str(e)}")
            
    st.header("📜 Transcript Viewer")
    if st.button("Load Transcript"):
        try:
            transcript = transcript_manager.load_youtube_transcript(TRANSCRIPT_YOUTUBE)
            transcript_corrected = llm_utils.youtube_french_sentence_generator(transcript)
            st.text_area("Transcript", value=transcript_corrected, height=300)
            
        except FileNotFoundError:
            st.error("Transcript file not found. Please extract a transcript first.")

    st.header("📜 Prompt viewer Viewer")
    if st.button("Show Prompt"):
        st.markdown(""" give me a numbered list of french sentneces from the pasted transcript""")
        st.markdown(""" Now give me english translation of the above sentences with same numbering and order""")
