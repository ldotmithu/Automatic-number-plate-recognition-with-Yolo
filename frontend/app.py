import streamlit as st
import requests
from PIL import Image
import io
import base64

st.title("🚗 Number Plate Recognition")

API_URL = "http://127.0.0.1:8000/predict"

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.subheader("Preview")
    st.image(uploaded, use_container_width=True)

    if st.button("Detect Plate"):
        files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
        resp = requests.post(API_URL, files=files)

        if resp.status_code == 200:
            data = resp.json()

            
            st.subheader("Result")
            img_bytes = base64.b64decode(data["image"])
            st.image(Image.open(io.BytesIO(img_bytes)), use_container_width=True)

            
            st.subheader("Extracted Plates")
            for i, plate in enumerate(data["plates"], 1):
                st.write(f"{i}. {plate}")
        else:
            st.error("Prediction failed")
