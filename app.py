import streamlit as st
from google import genai
import os
from api_calling import  generate_response,audio_transcription


response = ""

st.header("Easy Translator",anchor=None)

with st.form(key="my_form",  enter_to_submit=True):

    text = st.text_input("Text in any language",placeholder="Enter your words or sentences")
      
    selected = st.selectbox("Translate to ",
            ('Bangla','English','Korean','Hindi','Urdu'),
            index=2
    )
    clicked  = st.form_submit_button("Translate",type="primary")

st.set_page_config(page_title="Translator", layout="wide")

if clicked:

    if not text:
        st.error("Please enter some text ")
    if not selected:
        st.error("Please select your desire language")

    if text and selected:
        with st.container(border=True):
            st.subheader(f"Your text in {selected}")
            with st.spinner("Translating..."):
                response = generate_response(text,selected)
                st.markdown(response)


        with st.container(border=True):
            st.subheader("Audio",anchor=False)
            with st.spinner("AI is transcripting audio..."):
                st.audio(audio_transcription(response))
                # st.audio(audio_trascription("The audio will be transcripted soon"))

           
st.markdown("[More Apps ](https://github.com/monserali)!")
