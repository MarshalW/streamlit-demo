import streamlit as st

from streamlit_marshal_proto import proto

st.subheader("组件测试")
num_clicks = proto()
st.markdown(f"点击了 {num_clicks} 次")
