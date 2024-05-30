import streamlit as st
import json
from streamlit_lottie import st_lottie

def app():
    st.subheader('This is movie recommendation system')
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_coding = load_lottiefile("lottiefiles/boy.json")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=400,
        width= 1200,
        # width=50%,
        # background-color =transparent,
        key=None,
    )
    st.markdown(
        """
        <style>
            [data-testid="stFileUploader"] {
                # color: white;
                background-color: transparent;
                # border: none;
                # border-bottom: 1px solid white;
                # outline: none;
                # width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )