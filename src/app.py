import streamlit as st

pages = [
    st.Page("pages/main.py", title="Main"),
    st.Page("pages/players.py", title="Players stats"),
    st.Page("pages/teams.py", title="Teams stats"),
]

pg = st.navigation(pages)
pg.run()
