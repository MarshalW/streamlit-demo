import time
import streamlit as st

with st.status("下载数据...") as status:
    st.write("搜索数据...")
    time.sleep(2)
    st.write("找到 URL.")
    time.sleep(1)
    st.write("下载数据...")
    time.sleep(1)
    st.write("检查数据...")
    time.sleep(1)
    st.write("下载成功。")
    status.update(
        label="下载完毕!", state="complete", expanded=False
    )

st.button("重做")