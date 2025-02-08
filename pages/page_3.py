import streamlit as st
from statistics import mode

progress = 0
answers =[]
Question_1_Answered = False
Question_2_Answered = False
Question_3_Answered = False
Question_4_Answered = False
Question_5_Answered = False

#Results = False

#st.image("FemmHacks_2025/Images/clothing_header.jpg")
st.title("What's Your Style?")
st.subheader("Take this quiz to know what fashion sustainability practice suits you!")
Question_1_Answered = st.button("Start Quiz")

#def updateProgress(progress):
    # this is where the code for the progress bar goes
#    progress = progress + 1

if Question_1_Answered == True:
    progress = progress +1
    options = ["I wish I could customize this to fully express my style", 
                "I wish more people got the clothes they wanted",
                "I wonder what material this clothing is made of",
                "It'd be nice to pass this garment on to my grandchildren"]
    choice = st.radio("What’s the first thing you think of after buying new clothes?", options)
    answers.append(choice)
    if (choice!="-1"):
        Question_2_Answered = True
    


if Question_2_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["Adding designs to customize my outfit", 
                "Picking up trash at the local beach",
                "Volunteering at a shelter for vulnerable people",
                "Finding valuable items for a collection"]
    choice = st.radio("How would you like to spend a Saturday afternoon?", options)
    answers.append(choice)
    answers.append(choice)
    if (choice!="-1"):
        Question_3_Answered = True

if Question_3_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["Vintage Style", 
                "Practicality",
                "Comfort",
                "Durability"]
    choice = st.radio("What’s the most attractive quality an outfit can have?", options)
    answers.append(choice)
    if (choice!="-1"):
        Question_4_Answered = True

if Question_4_Answered == True:
    choice = "-1"
    progress = progress +1
    options = ["When someone is afraid to express themselves", 
                "When someone is afraid to express themselves",
                "When someone wastes their food",
                "When someone doesn’t plan for the long run"]
    choice = st.radio("What’s the first thing you think of after buying new clothes?", options)
    answers.append(choice)
    if (choice!="-1"):
        Question_5_Answered = True

if Question_5_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["It’s no longer my style", 
                "I’m giving it to a loved one",
                "I think it’s starting to look old",
                "It’s too damaged to maintain or repair"]
    choice = st.radio("Why would you want to get rid of a piece of clothing?", options)
    answers.append(choice)
    

if Results == True:
    uprogress = progress +1
    result = mode(answers)
    #thin image banner goes here eventually
    st.subheader("You are a...")
    if result == 0:
        st.title("Vintage Thrifter")
        st.write("You love to ")
    elif result == 1:
        st.title("Heartfelt Donor")
        st.write("info for giving clothes to vulnerable populations")
    elif result == 2:
        st.title("Garment Recycler")
        st.write("info about shops that sell recycled clothing")
    elif result == 3:
        st.title("Slow Fashionista")
        st.write("info about quality clothing stores and conscious consumerism")
    
    col1, col2 = st.columns(2)
    with col1:
        st.page_link("pages/page_1.py", label="Return Home")
    with col2:
        st.page_link("pages/page_3.py", label="Retry")

#st.image("FemmHacks_2025/Images/clothing_header.jpg")
#st.title("What's Your Style?")
#st.subheader("Take this quiz to know what fashion sustainability practice suits you!")
#st.button("Start Quiz", on_click=questionOne())

