import streamlit as st


#st.title("How to be a Sprout")
st.markdown("<h1 style='color: #467444;'>How to be a Sprout</h1>", unsafe_allow_html=True)
st.divider()

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.page_link("pages/page_2.py", label="Recycling", icon="♻️")

with col2:
     st.page_link("pages/page_3.py", label="Clothing", icon="👚")


with col3:
     st.page_link("pages/page_4.py", label="Composting", icon="🍄")
    
with col4:
     st.page_link("pages/page_5.py", label="Microplastics", icon="⚗️")

with col5:
     st.page_link("pages/page_6.py", label="Call to Action", icon="📢")



st.divider()

with st.container(border=True):

    #st.header("Our mission - SPROUT")
    st.markdown("<h2 style='color: #587056;'>Our mission - SPROUT</h2>", unsafe_allow_html=True)
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



st.divider()
with st.container(border=True):
    st.header("Why does taking care of the environment matters?")
    st.write("Taking care of the environment is crucial for our planet and future generations’s well-being. The natural world provides essential resources such as clean air, water, and food, which sustain life on Earth. By preserving ecosystems, we help ensure biodiversity and maintain the balance necessary for all living organisms (including us humans!) to thrive. In short, living in a healthy world makes it easier to live a healthy life.")

st.divider()
with st.container(border=True):
    st.header("What can you do?")
    st.write("While we all somewhat know how to recycle, and we should buy second-hand clothes, and maybe even compost, it is very confusing to know where to start and how to effectively help out. Our website is intended to guide you through ways you can help the Earth in your day-to-day life too. We recommend starting out with the recycling page and going from there.")
    st.page_link("pages/page_6.py", label="TAKE ACTION", icon="📢")
