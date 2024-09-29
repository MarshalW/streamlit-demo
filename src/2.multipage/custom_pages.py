import streamlit as st


def titles():
    return st.markdown(
        """
    <style>
:root {
  --text-color: #808495; /* Light text color */
  --bg-color: transparent; /* Dark background color */
}
a[href="http://ant:8502/"] span:first-child {
    position: relative;
    z-index: 1;
    color: transparent;
}
a[href="http://ant:8502/"] span:first-child::before {
    content: "首页";
    position: absolute;
    left: 0;
    z-index: 2;
    color: var(--text-color);
    background-color: var(--bg-color);
}
a[href="http://ant:8502/Page_two"] span:first-child {
    position: relative;
    z-index: 1;
    color: transparent;
}
a[href="http://ant:8502/Page_two"] span:first-child::before {
    content: "감자";
    position: absolute;
    left: 0;
    z-index: 2;
    color: var(--text-color);
    background-color: var(--bg-color);
}
a[href="http://ant:8502/About"] span:first-child {
    position: relative;
    z-index: 1;
    color: transparent;
}
a[href="http://ant:8502/About"] span:first-child::before {
    content: "주황색";
    position: absolute;
    left: 0;
    z-index: 2;
    color: var(--text-color);
    background-color: var(--bg-color);
}
a[href="http://ant:8502/Page_three"] span:first-child {
    position: relative;
    z-index: 1;
    color: transparent;
}
a[href="http://ant:8502/Page_three"] span:first-child::before {
    content: "사과";
    position: absolute;
    left: 0;
    z-index: 2;
    color: var(--text-color);
    background-color: var(--bg-color);
}
</style>
    """,
        unsafe_allow_html=True,
    )
