import streamlit as st

# задаем загаловок сайта
st.markdown(
    """<h1 style='text-align: center; color: black;'
            >Mumba Hub</h1>""",
    unsafe_allow_html=True,
)

st.write("""
         Данные взяты с сайта fbref и официального апи fantasy premiere league
    """)
