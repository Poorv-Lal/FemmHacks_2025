import streamlit as st

st.title("Recycling")

can_recycle = 0
message = ""


st.header("Want to know if you can recycle something?")
option = st.selectbox(
    "What kind of Material do you have?",
    ("Batteries/Electronics", "Carton", "Paper", "Cardboard","Food Scraps", "Glass","Plastic","Metal", "Styrofoam","Other/Unsure"),
    )

if option == "Paper":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Wet", "Shredded/In-small Pieces"),
    )

    if option2 == "Clean & Dry":
        can_recycle = 1
    elif option2 == "Wet":
        can_recycle = 0
        message = "but if it dries in one piece feel free to put it in there"
    elif option2 == "Shredded/In-small Pieces":
        can_recycle = 0
        message = "because it gets stuck in recycling plants"    
    
    
elif option == "Cardboard":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Dirty or Has food on it", "Shredded/In-small Pieces"),
    )

    if option2 == "Clean & Dry":
        can_recycle = 1
    elif option2 == "Dirty or Has food on it":
        can_recycle = 0
        message = "because the recycling plant cannot process dirty cardboard or food"
    elif option2 == "Shredded/In-small Pieces":
        can_recycle = 0
        message = "because it gets stuck in recycling plants" 

elif option == "Glass":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Wet", "Dirty"),
    )

    if option2 == "Clean & Dry":
        can_recycle = 1
    elif option2 == "Dirty":
        can_recycle = -1
        message = "Clean it and you are good to go"
    elif option2 == "Wet":
        can_recycle = -1
        message = "because it gets stuck in recycling plants" 

elif option == "Plastic":
    option2 = st.selectbox(
    "What Number is Located On inside the Recycle Symbol on the "+ option,
    ("1", "2", "3", "4", "5", "6","Other"),
    )
    
    if option2 == "1":
        can_recycle = 1
    elif option2 == "2":
        can_recycle = 1
    elif option2 == "3":
        can_recycle = 0
        message="because Philadelphia County does not what the capability to recycle this type of plastic"
    elif option2 == "4":
        can_recycle = 0
        message = "because Philadelphia County does not what the capability to recycle this type of plastic"
    elif option2 == "5":
        can_recycle = 1
        message = "because it gets stuck in recycling plants"
    elif option2 == "6":
        can_recycle = 0
        message = "because Philadelphia County does not what the capability to recycle this type of plastic"
    elif option2 == "Other":
        can_recycle = 0
        message = "because Philadelphia County does not what the capability to recycle this type of plastic"

elif option == "Metal":
    option2 = st.selectbox(
    "What type of Metal is it?",
    ("Bottle/jar Lid", "Aluminum, Steel, or Tin Can", "Paint or Aerosol Can", "Big Chunk", "Other/Unsure"),
    )

    if option2 == "Bottle/jar Lid":
        can_recycle = 1
    elif option2 == "Aluminum, Steel, or Tin Can":
        can_recycle = 1
    elif option2 == "Paint or Aerosol Can":
        on = st.toggle("Is it empty?")

        if on: 
            can_recycle = 1
        else:
            can_recycle = -1
            message="Empty it and then you can recycle it"
    elif option2 == "Big Chunk":
        can_recycle=0
        message="why???????"
    elif option2 == "Other/Unsure":
        can_recycle=0
        message="because if you are unsure what an item is or if it can be recycled, do NOT recycle it because any non-recyclable items will taint a whole batch of recycling at a plant"

        
    

elif option == "Batteries/Electronics":
    can_recycle = 0
    message = "because it is not normally recyclable, but local recycling plants near you may be able to handle or repurpose them"

elif option == "Carton":
    option2 = st.selectbox(
    "Is the " + option +" ______?",
    ("Clean & Dry","Wet", "Dirty"),
    )
    if option2 == "Clean & Dry":
        can_recycle = 1
    elif option2 == "Wet":
        can_recycle = -1
        message = "Dry it and you are good to go"
    elif option2 == "Diry":
        can_recycle = 1
        message = "Clean it and you are good to go"


elif option == "Food Scraps":
    can_recycle = 0
    message = "because food scraps are not recyclable, but if you have a household or local composting place you can try it there"

elif option == "Styrofoam":
    can_recycle = 0
    message = "because styrofoam is not recyclable, but local recycling plants may be able to repurpose it for other uses"

elif option == "Other/Unsure":
    can_recycle = 0
    message = "because if you are unsure what an item is or if it can be recycled, do NOT recycle it because any non-recyclable items will taint a whole batch of recycling at a plant"
 

if can_recycle == 1:
    st.success("♻️ You can Recycle this!!!")
elif can_recycle == -1:
    st.error("🤔 You might be able to Recycle this...")
elif can_recycle == 0:
    st.error("❌ You can NOT Recycled this...")
st.write(message)