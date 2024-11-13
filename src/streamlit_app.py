import streamlit as st

pages = [
    st.Page("main_page.py", title="Main"),
    st.Page("players.py", title="Players stats"),
    st.Page("teams.py", title="Teams stats"),
]

pg = st.navigation(pages)
pg.run()
