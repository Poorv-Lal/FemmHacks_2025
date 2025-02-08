import streamlit as st

st.title("Recycling")

with st.container(border=True):
    st.header("Want to know if you can recycle something?")
    st.page_link("pages/page_3.py", label="Recycle?", use_container_width=True)

st.divider()
with st.container(border=True):
    st.header("Take a Quiz to Test your Recycle Knowledge?")
    st.page_link("pages/page_3.py", label="Start Quiz", use_container_width=True)