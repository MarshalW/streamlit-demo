import streamlit as st

pg = st.navigation([
    st.Page("button.py", title="st.button"),
    # st.Page("dataframe.py", title="st.dataframe"),
    # st.Page("progress.py", title="st.progress"),
    # st.Page("status.py", title="st.status"),
    # st.Page("toast.py", title="st.toast"),
])

pg.run()