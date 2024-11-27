# streamlit run mainpage.py
import streamlit as st

# Set page config
st.set_page_config(layout="wide", page_title="AI Fun Zone", page_icon="🎭")

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

# Sidebar
with st.sidebar:
    st.title("AI Fun Zone 🎉")

st.title('AI Fun Zone에 오신 것을 환영합니다!')
tab1, tab2, tab3, tab4 = st.tabs(["닮은 연예인 찾기", "표정 공룡 게임", "MBTI 예측 로봇", "미로 게임"])

with tab1:
    st.markdown("""
    <h1>
        <a href="./celebrity" style="text-decoration: none; color: black;" target="_self">닮은 연예인 찾기🕵🏻‍♂️</a>
    </h1>
""", unsafe_allow_html=True)
    st.write('나와 닮은 연예인을 찾아봐요! 나의 웃는 표정과 무표정으로 닮은 연예인을 찾아봅시다!')
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <h1>
        <a href="./celebrity" style="text-decoration: none; color: black;" target="_self">닮은 연예인 찾기🕵🏻‍♂️</a>
    </h1>
""", unsafe_allow_html=True)
    st.image('./img/ido.png', use_column_width=True)

with tab2:
    st.markdown("""
    <h1>
        <a href="./dino" style="text-decoration: none; color: black;" target="_self">표정 공룡 게임🦖</a>
    </h1>
""", unsafe_allow_html=True)
    st.write("C로 시작하는 브라우저 사용자라면 안다는 유명한 공룡 게임! 이젠 표정으로 즐겨보세요!")
    st.markdown("<br>", unsafe_allow_html=True) 
    st.image('./img/dino.png', use_column_width=True)
    
with tab3:
    st.markdown("""
    <h1>
        <a href="./chatbot" style="text-decoration: none; color: black;" target="_self">MBTI 예측 로봇🤖</a>
    </h1>
""", unsafe_allow_html=True)
    st.write("이제 테스트는 그만! 사소한 정보로도 나의 MBTI를 예측하는 챗봇을 이용해보세요!")
    st.markdown("<br>", unsafe_allow_html=True) 
    st.image('./img/chatbot.jpg', use_column_width=True)
    
with tab4:
    st.markdown("""
    <h1>
        <a href="./maze" style="text-decoration: none; color: black;" target="_self">미로 게임 🛣️</a>
    </h1>
""", unsafe_allow_html=True)
    st.write("표정으로 미로를 풀어보세요! 감정을 표현하며 새로운 길을 찾아가세요!")
    st.markdown("<br>", unsafe_allow_html=True) 
    st.image('./img/maze.png', use_column_width=True)    

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