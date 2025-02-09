import streamlit as st
from collections import Counter

st.title("Clothing")


# Define quiz questions, options, and category mapping
quiz_data = [
    {
        "question": "What’s the first thing you think of after buying new clothes?",
        "options": {
            "I wish I could customize this to fully express my style": "Thrifting",
            "I wish more people got the clothes they wanted": "Donating",
            "I wonder what material this clothing is made of": "Recycling",
            "It’d be nice to pass this garment on to my grandchildren": "Slow fashion"
        }
    },
    {
        "question": "How would you like to spend a Saturday afternoon?",
        "options": {
            "Finding valuable items for a collection": "Slow fashion",
            " Picking up trash at the local beach": "Recycling",
            " Volunteering at a shelter for vulnerable people": "Donating",
            "Adding designs to customize my outfit": "Thrifting"
        }
    },
    {
        "question": "What’s the most attractive quality an outfit can have?",
        "options": {
            "Practicality": "Donating",
            "Durability": "Slow fashion",
            "Vintage Style": "Thrifting",
            "Comfort": "Recycling"
        }
    },
    {
        "question": "What’s a personal ick that you have?",
        "options": {
            "When someone wastes their food": "Recycling",
            "When someone is afraid to express themselves": "Thrifting",
            "When someone doesn’t plan for the long run": "Slow fashion",
            "When someone never shares with others": "Donating"
        }
    },
    {
        "question": "Why would you want to get rid of a piece of clothing?",
        "options": {
            "It’s too damaged to maintain or repair": "Slow fashion",
            "I think it’s starting to look old": "Recycling",
            "I’m giving it to a loved one": "Donating",
            "It’s no longer my style": "Thrifting"
        }
    }
]

# Personality categories and results
results = {
    "Thrifting": "Thrifting Answer",
    "Donating": "Donating Answer",
    "Recycling": "Recycling Answer",
    "Slow fashion": "Slow fashion Answer"
}

# Initialize session state
if "answers" not in st.session_state:
    st.session_state.answers = []

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Display quiz questions one at a time
if st.session_state.question_index < len(quiz_data):
    current_question = quiz_data[st.session_state.question_index]
    st.write(f"### {current_question['question']}")
    
    # Show radio button options
    selected_option = st.radio("Choose an answer:", list(current_question["options"].keys()), index=None)
    
    if st.button("Next"):
        if selected_option:
            st.session_state.answers.append(current_question["options"][selected_option])  # Store category
            st.session_state.question_index += 1
            st.rerun()
        else:
            st.warning("Please select an answer before proceeding!")

# Show final result when quiz is complete
else:
    st.write("## 🎉 Your Personality Result:")
    
    # Count the most frequent category
    personality_type = Counter(st.session_state.answers).most_common(1)[0][0]
    st.write(results[personality_type])

    # Reset quiz button
    if st.button("Restart Quiz"):
        st.session_state.answers = []
        st.session_state.question_index = 0
        st.rerun()
