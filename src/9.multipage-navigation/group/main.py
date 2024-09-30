import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    if st.button("登录"):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button("退出"):
        st.session_state.logged_in = False
        st.rerun()


login_page = st.Page(login, title="登录", icon=":material/login:")
logout_page = st.Page(logout, title="退出", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="工作台", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="报告错误", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="系统告警", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="搜索", icon=":material/search:")
history = st.Page("tools/history.py", title="历史", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "账号": [logout_page],
            "报告": [dashboard, bugs, alerts],
            "工具": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
