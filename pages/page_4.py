import streamlit as st

#st.title("Composting")
st.markdown("<h1 style='color: #467444;'>Composting</h1>", unsafe_allow_html=True)

with st.container(border=True):
    #st.header("What is Composting?")
    st.markdown("<h2 style='color: #587056;'>What is Composting?</h2>", unsafe_allow_html=True)
    st.write("Is the process of organic matter (like your food scraps) decomposing into compost. After going through the decomposition, compost can be added to soil to give plants nutrients.")


with st.container(border=True):
    #st.header("Can I compost?")
    st.markdown("<h2 style='color: #587056;'>Can I compost?</h2>", unsafe_allow_html=True)
    st.write("If you have room to compost in your backyard, great! If not check out your local area to see if there are gardens nearby that may be able to handle the space for composting.")
    

with st.container(border=True):
    #st.header("How to Compost?")
    st.markdown("<h2 style='color: #587056;'>How to Compost?</h2>", unsafe_allow_html=True)
    st.write("1)Pick a compost bin that works for you \n 2)Choose a sunny and flat spot for your bin to live \n 3)Alternate between layers of green and brown material (see below in tips what this means) \n 4)Lightly Wet the Compost when it is dry \n 5)Turn/Move around the compost once a week \n 6)Repeat steps 4-5 for about 3-4motnhs until the compost looks dark, crumbly, and smells like dirt")


with st.container(border=True):
    #st.header("Composting Tips")
    st.markdown("<h2 style='color: #587056;'>Composting Tips</h2>", unsafe_allow_html=True)
    st.write("- Make sure to have a mix of browns (dry leaves, plant stalks, shredded paper and cardboard, greens (fruit and vegetable scraps, grass clippings, coffee grounds, paper tea bags, and even eggshells), water for moisture, and lots of oxygen from the air.\n- Make sure that your composting container is locked so that rodents cannot make their way in\n- It takes about 3-4 months before compost is ready to use in soil\n- The compost pH should be between 6-8\n- If the compost is left too long or has fungi in it the compost is no longer usable")


with st.container(border=True):
    #st.header("What you CAN Compost")
    st.markdown("<h2 style='color: #587056;'>What you CAN Compost</h2>", unsafe_allow_html=True)
    st.write("- Fruit and vegetable peels and scraps\n- Rotten fruit and veggies\n- Houseplant trimmings\n- Coffee grounds and paper filters\n- Tea leaves\n- Eggshells\n- Nutshells (apart from walnuts)\n- Hair and fur\n -Paper, cardboard, and shredded newspaper\n- Napkins, paper towels, and unused toilet paper\n- Grass clippings\n- Leaves\n- Flowers\n- Sawdust\n- wood chips")


with st.container(border=True):
    #st.header("Do NOT Compost")
    st.markdown("<h2 style='color: #587056;'>Do NOT Compost</h2>", unsafe_allow_html=True)
    st.write("- Pet waste, such as feces or litter: may contain harmful bacteria or parasites\n- Bones or scraps from meat, fish, and poultry: produces odor and attracts pests\n- Dairy products: produces odor and attracts pests\n- Leaves or twigs from black walnut trees: releases a compound that’s toxic to plants\n Walnuts: releases a compound that’s toxic to plants\n- Coal ash or charcoal: contains compounds that may harm plants\n- Large pieces of wood: may take a long time to decompose\n- Fat, cooking oil, and grease: produces odor and attracts pests\n- Pesticide-treated lawn trimmings: may kill microorganisms needed for the composting process\n- Coffee pods: most contain plastic and don’t break down naturally\n- Baked goods: may attract pests and increase the growth of harmful bacteria\n- Plants that are diseased or infested with insects: may spread diseases")
