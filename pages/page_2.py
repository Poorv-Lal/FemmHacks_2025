import streamlit as st

st.title("Recycling")

st.header("Want to know if you can recycle something?")
with st.container(border=True):
    st.page_link("pages/recycling/materials", label="Recycle?", use_container_width=True)

st.divider()
st.header("Take a Quiz to Test your Recycle Knowledge?")
with st.container(border=True):
    st.page_link("pages/recycling/quiz", label="Start Quiz", use_container_width=True)