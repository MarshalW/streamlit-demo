import streamlit as st

from streamlit_marshal_helloworld import streamlit_marshal_helloworld

st.subheader("组件测试")
num_clicks =streamlit_marshal_helloworld()
st.markdown(f"点击了 {num_clicks} 次")