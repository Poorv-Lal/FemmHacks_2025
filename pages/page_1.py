import streamlit as st

# Custom CSS for container styles
st.markdown("""
    <style>
        .container-blue {
            background-color: #add8e6;  /* Light blue */
            padding: 20px;
            border-radius: 10px;
        }
        .container-green {
            background-color: #90ee90;  /* Light green */
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Homepage")
st.divider()

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.page_link("pages/page_2.py", label="Recycling", icon="♻️")

with col2:
     st.page_link("pages/page_3.py", label="Clothing", icon="👚")


with col3:
     st.page_link("pages/page_4.py", label="Composting", icon="🌱")
    
with col4:
     st.page_link("pages/page_5.py", label="Microplastics", icon="⚗️")

with col5:
     st.page_link("pages/page_6.py", label="Call to Action", icon="📢")





st.divider()
with st.container(border=True):
    st.markdown('<div class="container-green">', unsafe_allow_html=True)

    st.header("Our mission - SPROUT")
    st.subheader("Sustainability")
    st.write("Taking care of the earth in small ways where you can while meeting our individual and communal needs")
    st.subheader("Preservation")
    st.write("Not disturbing already existing green areas")
    st.subheader("Reducing,Reusing,&Recyling")
    st.write("Reducing our purchases where possible, Reusing them for years to come, and recycling properly")
    st.subheader("Outcomes")
    st.write("Not sweating the small stuff and focusing on the overall outcome of helping the planet where you can")
    st.subheader("Understanding ")
    st.write("Knowing where we can individually help out on smaller scales vs. taking collective action")
    st.subheader("Transitioning ")
    st.write("Taking the small steps gradual steps to change make green habits")
    
    st.markdown('</div>', unsafe_allow_html=True)


st.divider()
st.header("Why does taking care of the environment matters?")

st.divider()
st.header("What can you do?")