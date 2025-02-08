import streamlit as st

st.title("Recycling")

optionMaterial = st.selectbox(
    "What material are you tring to recycle?",
    ("Paper", "Carboard", "Glass", "Plastic","Metal","Batteries/Electronics", "Mixed Material", "Stryofoam", "Other", "Unsure"),
)

st.write("You selected:", optionMaterial)