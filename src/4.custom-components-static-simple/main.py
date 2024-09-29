import streamlit as st
import streamlit.components.v1 as components

st.write("静态自定义组件：")

components.html("<div>Hello</div>", height=200)

st.write("使用 iframe：")

components.iframe("https://news.163.com/", height=200)
# st.markdown('<iframe src="https://news.163.com/" />', unsafe_allow_html=True)
