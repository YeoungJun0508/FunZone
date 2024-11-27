import streamlit as st
from fuc import m_similarity_facial as m_sim
from fuc import w_similarity_facial as w_sim

st.set_page_config(layout="wide", page_title="닮은 연예인 찾기", page_icon="🕵️")
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

st.title('🕵️ 닮은 연예인 찾기 🕵️')
radio_select = st.sidebar.radio(
    "성별",
    ['남자', '여자'],
    horizontal=True
)

if 'Upicture' not in st.session_state:
    st.session_state.Upicture = None
    Tpicture1, Tpicture2 = None, None

if radio_select == "남자":
    print(st.session_state, "\n\n\n")
    if st.session_state.get('last_gender') != "남자":
        st.session_state.Upicture = None
        
    tab1, tab2 = st.tabs(["사진 업로드", "촬영하기"])
    with tab1:
        Upicture = st.file_uploader("사진 업로드", type=["jpg", "jpeg", "png"], key="upload1")
        if Upicture:
            st.session_state.Upicture = Upicture
            m_sim.sim1(Upicture)

    with tab2:
        Tpicture1, Tpicture2 = m_sim.capture_and_classify()
        if Tpicture1 is not None and Tpicture2 is not None:
            m_sim.sim2(Tpicture1, Tpicture2)

elif radio_select == "여자":
    if st.session_state.get('last_gender') != "여자":
        st.session_state.Upicture = None
        
    tab1, tab2 = st.tabs(["사진 업로드", "촬영하기"])
    with tab1:
        Upicture = st.file_uploader("사진 업로드", type=["jpg", "jpeg", "png"], key="upload2")
        if Upicture:
            st.session_state.Upicture = Upicture
            w_sim.sim1(Upicture)

    with tab2:
        Tpicture1, Tpicture2 = w_sim.capture_and_classify()
        if Tpicture1 is not None and Tpicture2 is not None:
            w_sim.sim2(Tpicture1, Tpicture2)

st.session_state.last_gender = radio_select

            
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