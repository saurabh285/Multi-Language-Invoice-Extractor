from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Multi Language Info Extractor")

st.header("Multi Language Info Extractor")

# User input field
input_text = st.text_input("Input Prompt:", key="input")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit = st.button("Tell me about the image")

# Prompt for Gemini
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image.
               """

# If button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        
        # Display response **before** the image
        response = get_gemini_response(input_prompt, image_data, input_text)
        st.subheader("The Response is:")
        st.write(response)

        # Now display the uploaded image below the response
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width=True)
    else:
        st.warning("Please upload an image before submitting.")
