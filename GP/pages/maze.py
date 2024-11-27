import streamlit as st
from fuc import mazestart as maze

# Set page config
st.set_page_config(layout="wide", page_title="미로 게임", page_icon="🛣️")

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem 3rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stTab {
        border-radius: 5px;
    }
    /*
    h1, h2, h3 {
        color: #ffffff; /* White text color for headers */
    }
    */
    .stSelectbox {
        margin-bottom: 20px;
    }
    .feature-container {
        background-color: #ffffff; /* White background color for feature containers */
        color: #000000; /* Black text color for feature container content */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .card {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        padding: 20px;
        margin: 20px;
        transition: transform 0.3s ease-in-out;
        cursor: pointer;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card-img {
        border-radius: 15px;
        margin-bottom: 10px;
    }
    .card-title {
        font-size: 1.5em;
        margin-bottom: 10px;
        color: #3366cc; /* Blue color for card titles */
    }
    .card-description {
        font-size: 1em;
        color: #666666; /* Gray color for card descriptions */
    }
    .details {
        margin-top: 20px;
        border-top: 2px solid #3366cc; /* Blue color for border */
        padding-top: 20px;
        color: #000000; /* Black text color for details section */
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #000000; /* Black text color for footer */
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛣️ 미로 게임 🛣️")
maze.startMaze()