import streamlit as st
from google import genai
import os
from api_calling import generate_response


with st.sidebar:
    st.header("Controls ",anchor=None)
    text = st.text_input("Enter Sentence")
    

    selected = st.selectbox("Translate to ",
        ('Bangla','English','Korean'),
        index=None
    )
    clicked  = st.button("Translate",type='primary')

st.header("Your personal translator",anchor=False)
st.text("Enter your text and hit on the button to translate")
st.divider()

if clicked:

    if not text:
        st.error("Please enter some text ")
    if not selected:
        st.error("Please select your desire language")

    if text and selected:
        with st.container(border=True):
            with st.spinner("Translating..."):
                response = generate_response(text,selected)
                st.markdown(response)

                


