import streamlit as st
from google import genai
import os
from api_calling import generate_response


response = ""

st.header("Easy Translator",anchor=None)
text = st.text_input("Enter Words/Sentences")
    

selected = st.selectbox("Translate to ",
        ('Bangla','English','Korean'),
        index=2
)
clicked  = st.button("Translate",type='primary')

st.set_page_config(page_title="Translator", layout="wide")
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


      with st.container(border=True):
            st.subheader("Audio",anchor=False)
            with st.spinner("AI is transcripting audio..."):
                st.audio(audio_transcription(text_for_audio,selected))
                # st.audio(audio_trascription("The audio will be transcripted soon"))

           
st.markdown("Created by Md Monser ")
