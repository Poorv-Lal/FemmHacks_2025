#Name: Ada Anya, Abbey Ham, Poorv Lal

import streamlit as st

st.Page("pages/materials.py",title="Materials")

pg = st.navigation([st.Page("pages/page_1.py",title="Homepage"),
                     st.Page("pages/page_2.py",title="Recycling"),
                     st.Page("pages/page_3.py",title="Clothing"),
                     st.Page("pages/page_4.py",title="Composting"),
                     st.Page("pages/page_5.py",title="Microplastics Avoiding"),
                     st.Page("pages/page_6.py",title="Call to Action")])
pg.run()
    






