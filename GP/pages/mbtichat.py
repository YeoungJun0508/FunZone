import streamlit as st
from fuc import mbtichatbot as chat

st.set_page_config(layout="wide", page_title="MBTI 예측 챗봇", page_icon="🤖")
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

st.title("🤖 MBTI 예측 챗봇 🤖")
st.markdown(
    """
    <p>
    이 챗봇은 간단한 취미나 취향 정보에 기반하여 MBTI 성격 유형을 예측합니다. 
    결과는 참고용으로만 사용되며, 전문적인 성격 분석 결과와는 다를 수 있습니다.
    </p>
    <p style='color:gray; font-size:small;'>MBTI 정보는 <a href='https://www.truity.com/' target='_blank'>Truity</a> 사이트를 참고하였습니다.</p>
    """, 
    unsafe_allow_html=True
)
chat.chatbot()

# Footer
st.markdown("""
    <style>
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