import streamlit as st

st.title("Recycling")

can_recycle = False


st.header("Want to know if you can recycle something?")
option = st.selectbox(
    "What kind of Material do you have?",
    ("Carton", "Paper", "Cardboard","Food Scraps", "Glass","Plastic","Metal","Styrofoam", "Other/Unsure"),
)

if option == "Carton":
    option2 = st.selectbox(
    "What kind of Material do you have?",
    ("Dry&Clean","Has Food On it", "Shredded/In-small Pieces"),
)
    
if can_recycle == 1:
    st.success("You can Recycle this!!!")
else:
    st.error("You can NOT Recycled this!!!")