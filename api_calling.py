from google import genai
import streamlit as st
import os,io
from dotenv import load_dotenv

from gtts import gTTS

load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def generate_response(text,option):
    try:
        prompt = f"Translate '{text}' to {option} give only the answer not much text"
        response = client.models.generate_content(
             model="gemini-3-flash-preview",
             contents=prompt
            )
        return response.text
        
    except Exception as e:
        print(e)
        return "Sorry. Something went wrong, Check and try again.."
   

def audio_trascription(txt,lan):
    speech = gTTS(txt,lang=lan)
    buffer = io.BytesIO()
    speech.write_to_fp(buffer)
    buffer.seek(0)
    return buffer