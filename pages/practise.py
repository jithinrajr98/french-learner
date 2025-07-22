import streamlit as st
from core.evaluation import check_translation
from core.transcript import TranscriptManager
from core.database import save_score, save_missing_words
from core.llm_utils import LLMUtils
from core.audio import play_audio

transcript_manager = TranscriptManager()
llm_utils = LLMUtils()

def render_practise():
    
    if 'current_pair' not in st.session_state:
        en, fr = transcript_manager.get_random_pair()
        st.session_state.update({
            'current_pair': (en, fr),
            'user_translation': "",
            'feedback': "",
            'checked': False,
            'score': 0
        })
    
    st.markdown(f"""
    <div class="card">
        <h3>Translate the following sentence:</h3>
        <p style="font-size:18px; color:#333;">📝 <strong>English</strong>: {st.session_state.current_pair[0]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_area(
        "✍️ Your French Translation:",
        value=st.session_state.user_translation,
        height=120,
        key="translation_area"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Check Translation", use_container_width=True):
            if user_input.strip():
                st.session_state.user_translation = user_input
                st.session_state.feedback, st.session_state.score = check_translation(
                    st.session_state.current_pair[0],
                    user_input,
                    st.session_state.current_pair[1]
                )
                missed = llm_utils.extract_missed_words(st.session_state.current_pair[1], user_input)
                if missed:
                    save_missing_words(missed)
                save_score(st.session_state.current_pair[0], user_input, st.session_state.score)
                st.session_state.checked = True
            else:
                st.warning("Please enter your translation.")

    with col2:
        if st.button("🔁 New Sentence", use_container_width=True):
            en, fr = transcript_manager.get_random_pair()
            st.session_state.current_pair = (en, fr)
            st.session_state.user_translation = ""
            st.session_state.feedback = ""
            st.session_state.checked = False
            st.session_state.score = 0
            st.rerun()

    if st.session_state.get("checked", False):
        
        st.markdown(f"""
        <div class="feedback">
            <h3>📋 Feedback</h3>
            <p><strong>Your attempt:</strong> {st.session_state.user_translation}</p>
        """, unsafe_allow_html=True)
        
        # Correct translation with audio
        correct_col1, correct_col2 = st.columns([4, 1])
        with correct_col1:
            st.markdown(f"<p>Correct:<strong> {st.session_state.current_pair[1]}</strong> </p>", unsafe_allow_html=True)
        
        play_audio(st.session_state.current_pair[1])

        st.markdown(f"""
            <p>{st.session_state.feedback}</p>
            <div class="score">Score: {st.session_state.score}/10</div>
        </div>
        """, unsafe_allow_html=True)



        
    
        