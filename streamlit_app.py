import streamlit as st
import requests
from PIL import Image
import io

st.title("Face with Glasses or Without Glasses Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    response = requests.post(
        "http://127.0.0.1:5000/predict",
        files={"file": ("image.jpg", img_bytes, "image/jpeg")}
    )

    if response.status_code == 200:
        prediction = response.json().get('prediction')
        if prediction == 1:
            st.write("Prediction: With Glasses")
        else:
            st.write("Prediction: Without Glasses")
    else:
        st.write("Error: ", response.json().get('error'))
