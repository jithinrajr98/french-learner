from config.styles import apply_custom_styles, header_section, sidebar_navigation, set_page_config
from core.database import init_db
from config.settings import DB_PATH
import streamlit as st
from pages.practise import render_practise
from pages.missed_words import render_missed_words
from pages.score_history import render_score_history
from pages.transcript_viewer import render_transcript
from pages.practise_missed_words import render_practise_missed_words

def main():
    set_page_config()
    apply_custom_styles()
    init_db(DB_PATH)
    header_section()
    page = sidebar_navigation()
    
    if page == "Practice":
        render_practise()
    if page == "Missed Words":
        render_missed_words()
    if page == "Score History":
        render_score_history()
    if page == "Transcript Viewer":
        render_transcript()
    if page == "Practice Missed Words":
        render_practise_missed_words()
   

if __name__ == "__main__":
    main()