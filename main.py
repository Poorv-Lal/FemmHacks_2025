#Name: Ada Anya, Abbey Ham, Poorv Lal

import streamlit as st

pg = st.navigation([st.Page("pages/page_1.py",title="Homepage"),
                     st.Page("page_2.py",title="Recycling"),
                     st.Page("page_3.py",title="Clothing"),
                     st.Page("page_4.py",title="Composting"),
                     st.Page("page_5.py",title="Microplastics Avoiding"),
                     st.Page("page_6.py",title="Call to Action")])
pg.run()
    






