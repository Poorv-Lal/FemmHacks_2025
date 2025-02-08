import streamlit as st

st.title("Recycling")

st.write("Want to know if you can recycle something?")
with st.container(border=True):
    st.button("Recycle?", type="primary", use_container_width=True)
    if st.button("Say hello"):
        st.write("Why hello there")

st.divider()
st.write("Take a Recyling Quiz to Test Your Knowledge?")
with st.container(border=True):
    st.button("Start Quiz", type="primary", use_container_width=True)
    if st.button("Say hello"):
        st.write("Why hello there")