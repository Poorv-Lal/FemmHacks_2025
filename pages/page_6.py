import streamlit as st

st.title("Call to Action")
st.subheader("Here's what you can do:")

# recycling
st.divider()
with st.container(border=True):
    st.subheader("Recycling Organizations and Practices")
    # info about recycling organizations and what to do goes here, and hyperlinks to companies
    st.write("information about companies in philly")
    col1, col2, col3 = st.columns(3)
    with col1:
        #first company, pls replace url
        st.page_link("pages/page_2.py", label="Company 1")
    with col2:
        #second company
        st.page_link("pages/page_2.py", label="Company 2")
    with col3:
        #third company
        st.page_link("pages/page_2.py", label="Company 3")
    
    st.write("summary about personal practices")
    st.page_link("pages/page_2.py", label="Recycling", icon="♻️")

# clothing
st.divider()
with st.container(border=True):
    st.header("Sustainable Fashion")
    st.write("information about companies who are trying to be sustainable")
    col1, col2, col3 = st.columns(3)
    with col1:
        #first company, pls replace url
        st.page_link("pages/page_3.py", label="Company 1")
    with col2:
        #second company
        st.page_link("pages/page_3.py", label="Company 2")
    with col3:
        #third company
        st.page_link("pages/page_3.py", label="Company 3")
    st.write("summary about personal practices")
    st.page_link("pages/page_3.py", label="Clothing", icon="👚")

# composting
st.divider()
with st.container(border=True):
    st.header("Sustainable Fashion")
    st.write("Composting is great if you have the resources to do so. If you don't have the space or time to compost, there are community gardens in Philadelphia that would happily take your green or brown matter.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("https://www.bennettcompost.com/how-it-works", label="Bennett Compost")
    with col2:
        st.page_link("https://drexel.campuslabs.com/engage/organization/drexelurbangrowers", label="Dornsife Community Garden")
    with col3:
        st.page_link("https://phsonline.org/programs/community-gardens", label="Philadelphia Horticultural Society")
    st.write("If you'd like to know more about composting and what materials to use, check out our composting page.")
    st.page_link("pages/page_4.py", label="Composting", icon="🍄")