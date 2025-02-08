import streamlit as st

st.title("Recycling")

st.header("Want to know if you can recycle something?")
with st.container(border=True):
    #st.page_link("pages/recycling/materials.py", label="Recycle?", use_container_width=True)
    st.page_link("Poorv-Lal/FemmHacks_2025/pages/recycling/materials.py", label="TAKE ACTION")

#st.divider()
#st.header("Take a Quiz to Test your Recycle Knowledge?")
#with st.container(border=True):
#    st.page_link("pages/recycling/quiz.py", label="Start Quiz", use_container_width=True)