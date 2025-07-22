import streamlit as st
from core.llm_utils import LLMUtils
from core.audio import play_audio
from core.database import save_score, save_missing_words,get_all_saved_words, delete_saved_word
import sqlite3
from config.settings import DB_PATH


llm_utils = LLMUtils()

def render_missed_words():
    
    st.title("📚 Missed Words")
    with st.form("add_word_form"):
        new_word = st.text_input("Enter a French word (minimum 4 letters):").strip()
        submitted = st.form_submit_button("Add Word")
        if submitted:
            if len(new_word) <= 3:
                st.warning("Word must be longer than 3 characters.")
            else:
                with sqlite3.connect(DB_PATH) as conn:
                    existing = conn.execute("SELECT 1 FROM missing_words WHERE word = ?", (new_word,)).fetchone()
                    if existing:
                        st.info(f"'{new_word}' is already in the list.")
                    else:
                        meaning = llm_utils.get_french_word_meaning(new_word)
                        conn.execute("INSERT INTO missing_words (word, meaning) VALUES (?, ?)", (new_word, meaning))
                        conn.commit()
                        st.success(f"'{new_word}' added with meaning: {meaning}")
                        st.rerun()
                                
    saved_words = get_all_saved_words()
    if saved_words:
        for word, meaning, timestamp in saved_words:
            cols = st.columns([3, 5, 1, 1])  # Added extra column for audio
            cols[0].markdown(f"<span style='font-size: 15px; font-weight: bold;'>{word}</span>", unsafe_allow_html=True)
            cols[1].markdown(f"<span style='font-size: 15px;'>{meaning}</span>", unsafe_allow_html=True)
            
            # Add audio playback button
            if cols[2].button("🔊", key=f"audio_{word}"):
                play_audio(word)
            
            if cols[3].button("❌", key=f"delete_{word}"):
                delete_saved_word(word)
                st.success(f"Deleted '{word}'")
                st.rerun()
    else:
        st.info("No missed words saved yet.")
            