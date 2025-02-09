import streamlit as st

#st.title("Call to Action")
st.markdown("<h1 style='color: #467444;'>Call to Action</h1>", unsafe_allow_html=True)
st.subheader("Lots of organizations are working towards a healthier environment for the future. Here's how you can help.")

# recycling
st.divider()
with st.container(border=True):
    st.subheader("Recycling Organizations and Practices")
    # info about recycling organizations and what to do goes here, and hyperlinks to companies
    st.write("Recycling on your own is important, but there's lots of fun when working with communities to reuse and sort disposables. You can get involved with some of these organizations.")
    col1, col2, col3 = st.columns(3)
    with col1:
        #first company, pls replace url
        st.page_link("https://prc.org/", label="Pennsylvania Research Council")
    with col2:
        #second company
        st.page_link("http://www.recyclenowphila.org/recycling_alliance.html", label="RecycleNow")
    with col3:
        #third company
        st.page_link("https://www.phila.gov/programs/tire-round-up-program/", label="Tire Round Up")
    
    st.write("If you'd like to know more about what materials are recyclable, check out our recycling page.")
    st.page_link("pages/page_2.py", label="Recycling", icon="♻️")

# clothing
st.divider()
with st.container(border=True):
    st.header("Sustainable Fashion")
    st.write("Cheaper clothes that don't last long are made in an industry process called \"fast fashion.\" This process was designed to keep up with the trends, but research has shown these practices damage the environment with non-biodegradable clothes. If you want to buy clothes that last longer, or are second-hand, check out these organizations. ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("https://www.habitatphiladelphia.org/restore/", label="habitat for Humanity")
    with col2:
        st.page_link("https://charlivintageandthrift.com/ ", label="Charli Vintage")
    with col3:
        st.page_link("https://www.heres2coolstuff.com/recycled", label="Here2Cool")
    st.write("If you'd like to know more sustainable fashion practices, check out our clothing page.")
    st.page_link("pages/page_3.py", label="Clothing", icon="👚")

# composting
st.divider()
with st.container(border=True):
    st.header("Composting")
    st.write("Composting is great if you have the resources to do so. If you don't have the space or time to compost, there are community gardens in Philadelphia that would happily take your green or brown matter.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("https://www.bennettcompost.com/how-it-works", label="Bennett Compost")
    with col2:
        st.page_link("https://drexel.campuslabs.com/engage/organization/drexelurbangrowers", label="Dornsife Community Garden")
    with col3:
        st.page_link("https://phsonline.org/programs/community-gardens", label="Philadelphia Horticultural Society")
    st.write("If you'd like to know more about composting, check out our composting page.")
    st.page_link("pages/page_4.py", label="Composting", icon="🍄")

# microplastics
st.divider()
with st.container(border=True):
    st.header("Microplastics")
    st.write("Microplastics are almost impossible to avoid in everyday life. Furthermore, they are super harmful to everything they come in contact with. It's important to join groups in Philadelphia focused on changing food production legislation to protect future geenrations.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link(" https://environmentamerica.org/pennsylvania/", label="PennEnvironment")
    with col2:
        st.page_link("https://cleanwater.org/states/pennsylvania", label="Clean Water Action")
    with col3:
        st.page_link(" https://mailchi.mp/ansp/plastic-free-philly", label="Plastic-Free Philly")
    st.write("If you'd like to know more about microplastics, check out our microplastics page.")
    st.page_link("pages/page_5.py", label="Microplastics", icon="⚗️")