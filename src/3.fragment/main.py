import streamlit as st
from streamlit.logger import get_logger

logger = get_logger(__name__)

st.title("我的应用")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
    logger.info("toggle and text")

toggle_and_text()


st.write("主要内容")
logger.info("main render")