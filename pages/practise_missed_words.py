import streamlit as st
from core.database import get_all_saved_words, delete_saved_word
import random
from core.audio import play_audio
from core.llm_utils import LLMUtils
import re

llm_utils = LLMUtils()

def render_practise_missed_words():
    st.title("🎯 Practice Missed Words")

    saved_words = get_all_saved_words()

    if not saved_words:
        st.info("No missed words available to practice yet.")
    else:
        if 'word_index' not in st.session_state:
            st.session_state.word_index = random.randint(0, len(saved_words) - 1)
            st.session_state.show_details = False

        current_word, current_meaning, _ = saved_words[st.session_state.word_index]

        st.markdown(f"### 🧩 : `{current_word}`")

        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 New Word"):
                st.session_state.word_index = random.randint(0, len(saved_words) - 1)
                st.session_state.show_details = False
                st.rerun()

        with col2:
            if st.button("👁️ Show Meaning & Conjugations"):
                st.session_state.show_details = True

        with col3:
            if st.button("🗑️ Delete Word"):
                delete_saved_word(current_word)  # You must define this function
                st.success(f"Deleted word: `{current_word}`")
                st.session_state.word_index = random.randint(0, max(0, len(saved_words) - 2))
                st.rerun()
                
        st.markdown("""
                        <style>
                            div[role=radiogroup] label {
                                margin-bottom: 15px;  /* Adjust this value as needed */
                                padding: 8px 12px;    /* Adds padding around each option */
                            }
                        </style>
                    """, unsafe_allow_html=True)
        # Add pronunciation button
        play_audio(current_word)
        
        if st.session_state.show_details:
            st.markdown(f"##### 📖 Meaning: `{current_meaning}`")
            st.markdown("""
                                <style>
                                    div[role=radiogroup] label {
                                        margin-bottom: 15px;  /* Adjust this value as needed */
                                        padding: 8px 12px;    /* Adds padding around each option */
                                    }
                                </style>
                            """, unsafe_allow_html=True)
            
            conjugation_response =llm_utils.get_word_details(current_word)
            example_sentence = llm_utils.example_generator(current_word)                    
            st.markdown("##### 🔁 Conjugation Info:")

            # Format response into readable lines
            st.markdown(conjugation_response)
            st.markdown("##### 📝 Example Sentence:")
            st.markdown(example_sentence)
            play_audio(example_sentence)

