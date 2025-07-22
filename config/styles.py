import streamlit as st

# ====== STYLE CONFIGURATION ======
def set_page_config():
    st.set_page_config(
        page_title="French Learner",
        page_icon="🇫🇷",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def apply_custom_styles():
    """Modern, elegant French-inspired theme with improved spacing and visual hierarchy"""
    french_blue = "#2C3E91"  # Deep French blue
    french_red = "#ED2939"   # French flag red
    french_cream = "#F8F4E9" # Soft cream background
    slate_gray = "#4A4A4A"   # Elegant text color
    
    st.markdown(f"""
    <style>
        /* Main app container */
        .stApp {{
            background-color: {french_cream};
            color: {slate_gray};
            font-family: 'Inter', sans-serif;
        }}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {french_blue} 0%, #1A2C6E 100%);
            color: white;
        }}
        
        /* Navigation menu items */
        div[role=radiogroup] > label {{
            margin: 8px 0;
            padding: 12px 16px;
            border-radius: 8px;
            background: rgba(255,255,255,0.1);
            color: white !important;
            transition: all 0.3s ease;
        }}
        
        div[role=radiogroup] > label:hover {{
            background: rgba(255,255,255,0.2);
            transform: translateX(4px);
        }}
        
        div[role=radiogroup] > [data-baseweb="radio"]:checked + label {{
            background: {french_red};
            font-weight: 500;
        }}
        
        /* Buttons */
        .stButton > button {{
            border-radius: 8px;
            padding: 10px 24px;
            background: linear-gradient(90deg, {french_blue} 0%, {french_red} 100%);
            color: white;
            border: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(44, 62, 145, 0.2);
        }}
        
        /* Headers */
        h1 {{
            color: {french_blue};
            font-weight: 500;
            letter-spacing: -0.5px;
            margin-bottom: 0.5rem;
        }}
        
        h2 {{
            color: {french_blue};
            font-weight: 400;
            border-bottom: 2px solid {french_red};
            padding-bottom: 6px;
            margin-top: 1.5rem;
        }}
        
        /* Input fields */
        .stTextArea textarea, .stTextInput input {{
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #ddd;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}
        
        /* Cards */
        .card {{
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border: 1px solid rgba(0,0,0,0.05);
        }}
        
        /* Feedback section */
        .feedback {{
            background: white;
            border-left: 4px solid {french_blue};
            padding: 18px;
            border-radius: 0 8px 8px 0;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        
        /* Score display */
        .score {{
            font-size: 1.6rem;
            font-weight: 700;
            color: {french_blue};
            text-align: center;
            margin: 16px 0;
            padding: 8px;
            background: rgba(44, 62, 145, 0.1);
            border-radius: 8px;
        }}
        
        /* Word cards */
        .word-card {{
            background: white;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
            transition: all 0.3s ease;
            border-left: 3px solid {french_blue};
        }}
        
        .word-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {french_cream};
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: {french_blue};
            border-radius: 4px;
        }}
    </style>
    """, unsafe_allow_html=True)

# ====== UI COMPONENTS ======
def header_section():
    """Elegant header with perfectly aligned French flag and title"""
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: center; height: 100%; padding-top: 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg" 
                     width="72" style="display: block;">
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown("""
        <div style="margin-top: 10px;">
            <h1 style="margin-bottom: 0; padding-top: 0;">French Mastery</h1>
            <p style="color: #666; font-size: 0.95rem; margin-top: -8px;">
                Apprendre le français avec intelligence artificielle
            </p>
        </div>
        """, unsafe_allow_html=True)

def sidebar_navigation():
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align:top; margin-bottom:20px;">
            <h3 style="color:#635BFF;">📚 Menu</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # page = st.radio(
        #     "Go to:",
        #     ["Practice", "Missed Words", "Score History", "Transcript Viewer", "Practice Missed Words"],
        #     label_visibility="collapsed"
        # )
        
         # Put widgets inside a container
        with st.container():
            page = st.radio(
                "",  # No label
                ["Practice", "Missed Words", "Score History", "Transcript Viewer", "Practice Missed Words"],
                label_visibility="collapsed"
            )

        st.markdown("---")
        st.markdown("""
        <div style="text-align:center; margin-top:20px; font-size: 0.8rem; color: #888;">
            <small>Built by Jithin</small>
        </div>
        """, unsafe_allow_html=True)

    return page
    

















# import streamlit as st
# # ====== STYLE CONFIGURATION ======
# def set_page_config():
#     st.set_page_config(
#         page_title="French Learner",
#         page_icon="🇫🇷",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )


# def apply_custom_styles():
#     # Claude-inspired color palette
#     background_color = "#FAF9F6"  # light beige
#     sidebar_color = "#F4F4F5"
#     primary_color = "#635BFF"     # Claude accent (soft indigo)
#     secondary_color = "#3E3E3E"
#     card_background = "#FFFFFF"
#     text_color = "#2C2C2C"

#     st.markdown(f"""
#     <style>
#         /* Main app background */
#         section[data-testid="stApp"] {{
#             background-color: {background_color};
#             color: {text_color};
#             font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
#         }}

#         /* Sidebar */
#         [data-testid="stSidebar"] {{
#             background-color: {sidebar_color};
#         }}

#         /* Radio buttons */
#         div[role=radiogroup] label {{
#             margin-bottom: 12px;
#             padding: 8px 14px;
#             border-radius: 6px;
#             background: #ffffff;
#             border: 1px solid #DDD;
#             transition: all 0.2s ease;
#             font-size: 0.95rem;
#             color: {text_color};
#         }}

#         div[role=radiogroup] label:hover {{
#             background: {primary_color}10;
#             border-left: 3px solid {primary_color};
#         }}

#         /* Buttons */
#         .stButton > button {{
#             border-radius: 6px;
#             padding: 10px 20px;
#             font-weight: 500;
#             font-size: 0.95rem;
#             color: white;
#             background-color: {primary_color};
#             border: none;
#             transition: all 0.2s ease;
#         }}

#         .stButton > button:hover {{
#             background-color: #4E46E5;
#             box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
#         }}

#         /* Headers */
#         h1 {{
#             color: {primary_color};
#             font-weight: 600;
#             padding-bottom: 4px;
#         }}

#         h2 {{
#             color: {secondary_color};
#             font-weight: 500;
#         }}

#         /* Text areas */
#         .stTextArea textarea {{
#             border-radius: 6px;
#             padding: 10px;
#             background-color: #fff;
#             border: 1px solid #ddd;
#         }}

#         /* Cards */
#         .card {{
#             background: {card_background};
#             border-radius: 8px;
#             padding: 18px;
#             margin-bottom: 18px;
#             box-shadow: 0 2px 5px rgba(0,0,0,0.03);
#         }}

#         /* Feedback section */
#         .feedback {{
#             background: #F8F9FA;
#             border-left: 4px solid {primary_color};
#             padding: 14px;
#             border-radius: 4px;
#             margin: 15px 0;
#         }}

#         /* Score display */
#         .score {{
#             font-size: 1.4rem;
#             font-weight: 600;
#             color: {primary_color};
#             text-align: center;
#             margin: 12px 0;
#         }}

#         /* Word cards */
#         .word-card {{
#             background: {card_background};
#             border-radius: 6px;
#             padding: 12px;
#             margin-bottom: 10px;
#             box-shadow: 0 1px 4px rgba(0,0,0,0.04);
#             transition: all 0.2s ease;
#         }}

#         .word-card:hover {{
#             transform: translateY(-2px);
#             box-shadow: 0 3px 8px rgba(0,0,0,0.08);
#         }}
#     </style>
#     """, unsafe_allow_html=True)




# # ====== UI COMPONENTS ======
# def header_section():
#     col1, col2 = st.columns([1, 4])
#     with col1:
#         st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg", width=64)
#     with col2:
#         st.markdown("""
#         <div style="margin-top: 6px;">
#             <h1 style="margin-bottom: 0;">The Limiting Factor</h1>
#             <p style="color: #666; font-size: 0.9rem; margin-top: 4px;">AI assistance</p>
#         </div>
#         """, unsafe_allow_html=True)


# def sidebar_navigation():
#     with st.sidebar:
#         st.markdown(f"""
#         <div style="text-align:top; margin-bottom:20px;">
#             <h3 style="color:#635BFF;">📚 Menu</h3>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # page = st.radio(
#         #     "Go to:",
#         #     ["Practice", "Missed Words", "Score History", "Transcript Viewer", "Practice Missed Words"],
#         #     label_visibility="collapsed"
#         # )
        
#          # Put widgets inside a container
#         with st.container():
#             page = st.radio(
#                 "",  # No label
#                 ["Practice", "Missed Words", "Score History", "Transcript Viewer", "Practice Missed Words"],
#                 label_visibility="collapsed"
#             )

#         st.markdown("---")
#         st.markdown("""
#         <div style="text-align:center; margin-top:20px; font-size: 0.8rem; color: #888;">
#             <small>Built by Jithin</small>
#         </div>
#         """, unsafe_allow_html=True)

#     return page
    