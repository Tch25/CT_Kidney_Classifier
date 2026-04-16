import streamlit as st
#Send HTTP requests to the FastAPI backend
import requests
from PIL import Image
import io

#---Configuration---
set.set_page_config(
    page_title = "Kidney CT Analyezer"
    page_icon = "🩻"
    layout = "wide"
)

#---App header and description---
st.title("🩻 Kidney CT Scan Analyzer")
st.markdown("Upload a CT scan to detect **Cysts**, **Tumors** or **Stones**")

#---URL of the API---
API_URL = st.text_input("API URL:", value="http://localhost:8000")  #Using local for testing
