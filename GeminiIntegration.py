import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


GEMINI_KEY = st.secrets["GEMINI_KEY"]

if not GEMINI_KEY:
    st.error("API Key not found! Add it to Streamlit Secrets.")
else:
    st.success("API Key loaded successfully!")

try:
    genai.configure(api_key=GEMINI_KEY)
except Exception as e:
    st.error(f"Failed to configure Gemini API: {e}")

try:
    genai.configure(api_key=GEMINI_KEY)
except Exception as e:
    st.error(f"Failed to configure Gemini API: {e}")


def get_gemini_response(input_text, image):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([input_text, image])
        return response.text
    except Exception as e:
        st.error(f"Error generating content with Gemini: {e}")
        return None
