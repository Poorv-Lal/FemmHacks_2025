import streamlit as st

st.title("Recycling")

can_recycle = 0
message = ""


st.header("Want to know if you can recycle something?")
option = st.selectbox(
    "What kind of Material do you have?",
    ("Carton", "Paper", "Cardboard","Food Scraps", "Glass","Plastic","Metal","Styrofoam", "Other/Unsure"),
    )

if option == "Paper":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Wet", "Shredded/In-small Pieces"),
    )

    if option2 == "Clean & Dry":
        can_recycle = 1
    
elif option == "Carton":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Has Food On it", "Shredded/In-small Pieces"),
    )

elif option == "Cardboard":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Have Food On it", "Shredded/In-small Pieces"),
    )
    
if can_recycle == 1:
    st.success("You can Recycle this!!! ♻️")
elif can_recycle == -1:
    st.error("You might be able to Recycle this!!! 🤔")
elif can_recycle == 0:
    st.error("You can NOT Recycled this!!!❌")