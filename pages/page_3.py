import streamlit as st
from statistics import mode

'''
progress = 0
answers =[]
Question_1_Answered = False
Question_2_Answered = False
Question_3_Answered = False
Question_4_Answered = False
Question_5_Answered = False

Results = False

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
    Question_2_Answered = st.button("Next Question")


if Question_2_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["Adding designs to customize my outfit", 
                "Picking up trash at the local beach",
                "Volunteering at a shelter for vulnerable people",
                "Finding valuable items for a collection"]
    choice = st.radio("How would you like to spend a Saturday afternoon?", options)
    answers.append(choice)
    Question_3_Answered = st.button("Next Question")

if Question_3_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["Vintage Style", 
                "Practicality",
                "Comfort",
                "Durability"]
    choice = st.radio("What’s the most attractive quality an outfit can have?", options)
    answers.append(choice)
    Question_4_Answered = st.button("Next Question")

if Question_4_Answered == True:
    choice = "-1"
    progress = progress +1
    options = ["When someone is afraid to express themselves", 
                "When someone is afraid to express themselves",
                "When someone wastes their food",
                "When someone doesn’t plan for the long run"]
    choice = st.radio("What’s the first thing you think of after buying new clothes?", options)
    answers.append(choice)
    Question_5_Answered = st.button("Next Question")

if Question_5_Answered == True:
    choice = "-1"
    progress = progress + 1
    options = ["It’s no longer my style", 
                "I’m giving it to a loved one",
                "I think it’s starting to look old",
                "It’s too damaged to maintain or repair"]
    choice = st.radio("Why would you want to get rid of a piece of clothing?", options)
    answers.append(choice)
    Results = st.button("Get Results")

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

'''

# Define quiz questions and answers
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": "12"},
]

# Initialize session state variables
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# Get current question
current_question = quiz_data[st.session_state.question_index]

st.write(f"### Question {st.session_state.question_index + 1}: {current_question['question']}")

# Display options as buttons
for option in current_question["options"]:
    if st.button(option, key=option):
        if not st.session_state.answered:  # Prevent multiple submissions
            st.session_state.answered = True
            if option == current_question["answer"]:
                st.success("Correct! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! The correct answer is {current_question['answer']}.")

# Show "Next Question" button if answered
if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.question_index += 1
        st.session_state.answered = False  # Reset answer state
        if st.session_state.question_index >= len(quiz_data):  # Check if quiz is over
            st.write(f"### Quiz Complete! Your score: {st.session_state.score}/{len(quiz_data)}")
            st.session_state.question_index = 0  # Reset for restart
            st.session_state.score = 0
        st.rerun()
