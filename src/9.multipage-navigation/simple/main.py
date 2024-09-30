import streamlit as st

pg = st.navigation([
    st.Page("page_1.py", title="创建条目", icon=":material/add_circle:"),
    st.Page("page_2.py", title="条目列表", icon=":material/list:"),
])

pg.run()
