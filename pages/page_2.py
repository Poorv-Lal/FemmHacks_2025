import streamlit as st

st.title("Recycling")

st.write("Want to know if you can recycle something?")
st.button("Recycle?", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")