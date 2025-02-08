#Name: Ada Anya, Abbey Ham, Poorv Lal

import streamlit as st 

# HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
# hey!

if __name__ == "__main__":
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.navigation("Go to", ["Home", "Page 1", "Page 2"])

    # Home page content
    if page == "Home":
        st.title("Home Page")
        st.write("Ahhhhhh")  # Display "Ahhhhhh" on the Home page

    # Page 1 content
    elif page == "Page 1":
        st.title("Page 1: About Us")
        st.write("This is the first additional page.")

    # Page 2 content
    elif page == "Page 2":
        st.title("Page 2: Contact")
        st.write("This is the second additional page.")
    






