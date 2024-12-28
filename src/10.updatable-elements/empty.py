import streamlit as st
from streamlit.logger import get_logger

logger = get_logger(__name__)

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
# with placeholder.container():
#     st.write("This is one element")
#     st.write("This is another")

# Clear all those elements:
# placeholder.empty()

logger.info(">>>>>>> This is an info level log message~~")