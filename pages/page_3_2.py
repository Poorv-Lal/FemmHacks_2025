import streamlit as st
from collections import Counter

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
        "question": "What's your favorite type of movie?",
        "options": {
            "🎭 Drama": "Curious",
            "😂 Comedy": "Relaxed",
            "🎬 Action": "Adventurous",
            "🎀 Romance": "Cozy"
        }
    },
    {
        "question": "How do you spend a Sunday?",
        "options": {
            "🌲 Hiking or outdoor adventures": "Adventurous",
            "📖 Reading a book": "Curious",
            "🍿 Watching Netflix": "Cozy",
            "🧘‍♂️ Relaxing with music": "Relaxed"
        }
    }
]

# Personality categories and results
results = {
    "Relaxed": "🌴 You have a **chill and laid-back** personality! You enjoy life at your own pace.",
    "Adventurous": "⛰️ You’re a **thrill-seeker**! You love new experiences and taking risks.",
    "Curious": "🔍 You have a **curious mind**! You're always exploring and learning new things.",
    "Cozy": "☕ You love **comfort**! Whether it’s books, warm blankets, or cozy nights in."
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
