import time
import json
import streamlit as st
from PIL import Image
from Input import input_value
import DisplayDetails
import Helper as hp
import GeminiIntegration as gi


def image_upload():

    st.subheader("Upload Receipt Image to Analyse...")
    uploaded_file = st.file_uploader(
        "Upload a Receipt...", type=["jpg", "jpeg", "png"])
    image = None

    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            # st.image(image, caption="Uploaded Image", use_container_width=True)
            # Resize image to a fixed height (e.g., 300px) while maintaining aspect ratio
            new_height = 400
            width, height = image.size
            # Maintain aspect ratio
            new_width = int((new_height / height) * width)
            resized_image = image.resize((new_width, new_height))

            # Display resized image
            st.image(resized_image, caption="Resized Image",
                     use_container_width=False)

        except Exception as e:
            st.error(f"Error processing the uploaded file: {e}")

    if st.button("Analyse Uploaded Receipt"):
        if not uploaded_file:
            st.error("Please upload an image to proceed.")
        else:
            try:
                with st.spinner('Processing receipt...'):
                    enhanced_image = hp.enhance_image(image)

                    start_time = time.time()
                    response = gi.get_gemini_response(
                        input_value, enhanced_image)
                    elapsed_time = time.time() - start_time

                    if response:
                        st.info(
                            f"Time Taken: {elapsed_time:.2f} seconds", icon="⌚")
                        json_string = hp.clean_response(response)

                        if json_string:
                            try:
                                json_data = json.loads(json_string)
                                json_data = hp.clean_numeric_values(json_data)

                                updated_json_data = DisplayDetails.print_response_from_image(
                                    json_data)

                            except json.JSONDecodeError as e:
                                st.error(f"Error decoding JSON: {e}")
                        else:
                            st.error("Cleaned JSON response is empty.")
                    else:
                        st.error("No response received from the Gemini API.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# # import time
# # import json
# # import streamlit as st
# # from PIL import Image, ImageEnhance, ImageFilter
# # from Input import input_value
# # import DisplayDetails
# # import Helper as hp
# # import GeminiIntegration as gi


# # def set_dark_theme():
# #     """Set custom dark theme for the Streamlit application"""
# #     st.markdown("""
# #     <style>
# #     /* Dark theme base styles */
# #     body {
# #         color: white !important;
# #         background-color: #121212;
# #     }

# #     /* Streamlit specific overrides */
# #     .stApp {
# #         background-color: #121212;
# #         color: white !important;
# #     }

# #     /* Ensure all text is white */
# #     * {
# #         color: white !important;
# #     }

# #     /* Header styling */
# #     h1, h2, h3, h4, h5, h6 {
# #         color: rgb(255, 75, 75) !important;
# #     }

# #     /* File uploader container styling */
# #     .stFileUploader {
# #         background-color: #1e1e1e !important;
# #         border: 2px solid #3a3a3a !important;
# #         border-radius: 10px !important;
# #         padding: 15px !important;
# #     }

# #     .stFileUploader > div {
# #         background-color: #2a2a2a !important;
# #         border-radius: 8px !important;
# #     }

# #     .stFileUploader > div > div > div {
# #         background-color: #2a2a2a !important;
# #     }

# #     .stFileUploader > div > div > div > input {
# #         background-color: #2a2a2a !important;
# #         color: white !important;
# #         border: 1px solid #4a4a4a !important;
# #         border-radius: 6px !important;
# #     }

# #     /* Drag and drop text */
# #     .stFileUploader > div > div > div > p {
# #         color: #a0a0a0 !important;
# #     }

# #     /* Image container styling */
# #     .stImage {
# #         border: 2px solid #2a2a2a;
# #         border-radius: 8px;
# #         background-color: #1e1e1e !important;
# #         padding: 10px;
# #     }

# #     /* Button styling */
# #     .stButton > button {
# #         background-color: rgb(255, 75, 75) !important;
# #         color: white !important;
# #         border: none;
# #         transition: all 0.3s ease;
# #     }

# #     .stButton > button:hover {
# #         background-color: rgb(255, 100, 100) !important;
# #         transform: scale(1.05);
# #     }

# #     /* Spinner and info box styling */
# #     .stSpinner > div > div {
# #         border-color: rgb(255, 75, 75) !important;
# #     }

# #     .stAlert {
# #         background-color: #2a2a2a !important;
# #         color: white !important;
# #         border-left: 4px solid rgb(255, 75, 75) !important;
# #     }

# #     /* Error message styling */
# #     .stException {
# #         background-color: #2a2a2a !important;
# #         color: white !important;
# #         border-left: 4px solid red !important;
# #     }
# #     </>
# #     """, unsafe_allow_html=True)


# # def image_upload():
# #     # Apply dark theme
# #     set_dark_theme()

# #     # Subheader with dark theme color
# #     st.markdown("<h2>Upload Receipt Image to Analyse...</h2>",
# #                 unsafe_allow_html=True)

# #     uploaded_file = st.file_uploader(
# #         "Upload a Receipt...", type=["jpg", "jpeg", "png"])
# #     image = None

# #     if uploaded_file:
# #         try:
# #             image = Image.open(uploaded_file)
# #             st.image(image, caption="Uploaded Image", use_container_width=True)

# #         except Exception as e:
# #             st.error(f"Error processing the uploaded file: {e}")

# #     if st.button("Analyse Uploaded Receipt"):
# #         if not uploaded_file:
# #             st.error("Please upload an image to proceed.")
# #         else:
# #             try:
# #                 with st.spinner('Processing receipt...'):
# #                     enhanced_image = hp.enhance_image(image)

# #                     start_time = time.time()
# #                     response = gi.get_gemini_response(
# #                         input_value, enhanced_image)
# #                     elapsed_time = time.time() - start_time

# #                     if response:
# #                         st.info(
# #                             f"Time Taken: {elapsed_time:.2f} seconds", icon="⌚")
# #                         json_string = hp.clean_response(response)

# #                         if json_string:
# #                             try:
# #                                 json_data = json.loads(json_string)
# #                                 json_data = hp.clean_numeric_values(json_data)

# #                                 updated_json_data = DisplayDetails.print_response_from_image(
# #                                     json_data)

# #                             except json.JSONDecodeError as e:
# #                                 st.error(f"Error decoding JSON: {e}")
# #                         else:
# #                             st.error("Cleaned JSON response is empty.")
# #                     else:
# #                         st.error("No response received from the Gemini API.")
# #             except Exception as e:
# #                 st.error(f"An error occurred: {e}")
# import time
# import json
# import streamlit as st
# from PIL import Image, ImageEnhance, ImageFilter
# from Input import input_value
# import DisplayDetails
# import Helper as hp
# import GeminiIntegration as gi


# # def set_dark_theme():
# #     """Set custom dark theme for the Streamlit application"""
# #     st.markdown("""
# #     <style>
# #     /* Dark theme base styles */
# #     body {
# #         color: white !important;
# #         background-color: black;
# #     }

# #     /* Streamlit specific overrides */
# #     .stApp {
# #         background-color: black;
# #         color: white !important;
# #     }

# #     /* Ensure all text is white */
# #     * {
# #         color: white !important;
# #     }

# #     /* Header styling */
# #     h1, h2, h3, h4, h5, h6 {
# #         color: rgb(255, 75, 75) !important;
# #     }

# #     /* File uploader container styling */
# #     .stFileUploader {
# #         background-color: black !important;
# #         border: 2px solid black !important;
# #         border-radius: 10px !important;
# #         padding: 15px !important;
# #     }

# #     .stFileUploader > div {
# #         background-color: black !important;
# #         border-radius: 8px !important;
# #     }

# #     .stFileUploader > div > div > div {
# #         background-color: black !important;
# #     }

# #     .stFileUploader > div > div > div > input {
# #         background-color: black !important;
# #         color: white !important;
# #         border: 1px solid black !important;
# #         border-radius: 6px !important;
# #     }

# #     /* Drag and drop text */
# #     .stFileUploader > div > div > div > p {
# #         color: #a0a0a0 !important;
# #     }

# #     /* Image container styling */
# #     .stImage {
# #         border: 2px solid black;
# #         border-radius: 8px;
# #         background-color: black !important;
# #         padding: 10px;
# #     }

# #     /* Button styling */
# #     .stButton > button {
# #         background-color: rgb(255, 75, 75) !important;
# #         color: white !important;
# #         border: none;
# #         transition: all 0.3s ease;
# #     }

# #     .stButton > button:hover {
# #         background-color: rgb(255, 100, 100) !important;
# #         transform: scale(1.05);
# #     }

# #     /* Spinner and info box styling */
# #     .stSpinner > div > div {
# #         border-color: rgb(255, 75, 75) !important;
# #     }

# #     .stAlert {
# #         background-color: black !important;
# #         color: white !important;
# #         border-left: 4px solid rgb(255, 75, 75) !important;
# #     }

# #     /* Error message styling */
# #     .stException {
# #         background-color: black !important;
# #         color: white !important;
# #         border-left: 4px solid red !important;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# def set_dark_theme():
#     """Set custom dark theme for the Streamlit application"""
#     st.markdown("""
#     <style>
#     /* File uploader container styling */
#     .stFileUploader {
#         background-color: black !important;
#         border: 2px solid black !important;
#         border-radius: 10px !important;
#         padding: 15px !important;
#     }

#     .stFileUploader > div {
#         background-color: black !important;
#         border-radius: 8px !important;
#     }

#     .stFileUploader > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div > input {
#         background-color: black !important;
#         color: white !important;
#         border: 1px solid #333 !important;
#         border-radius: 6px !important;
#     }

#     /* Drag and drop text */
#     .stFileUploader > div > div > div > p {
#         color: #888 !important;
#     }
#     .e17y52ym0{
#         background-color: #2a2a2a !important;

#     }
#     .em9zgd02{
#         background-color: #ff4b4b !important;
#     }
#     .e5tuigk0{
#         background-color: #2a2a2a !important;
#     }

#     </style>
#     """, unsafe_allow_html=True)


# def image_upload():
#     # Apply dark theme
#     set_dark_theme()

#     # Subheader with dark theme color
#     st.markdown("<h2>Upload Receipt Image to Analyse...</h2>",
#                 unsafe_allow_html=True)

#     uploaded_file = st.file_uploader(
#         "Upload a Receipt...", type=["jpg", "jpeg", "png"])
#     image = None

#     if uploaded_file:
#         try:
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_container_width=True)

#         except Exception as e:
#             st.error(f"Error processing the uploaded file: {e}")

#     if st.button("Analyse Uploaded Receipt"):
#         if not uploaded_file:
#             st.error("Please upload an image to proceed.")
#         else:
#             try:
#                 with st.spinner('Processing receipt...'):
#                     enhanced_image = hp.enhance_image(image)

#                     start_time = time.time()
#                     response = gi.get_gemini_response(
#                         input_value, enhanced_image)
#                     elapsed_time = time.time() - start_time

#                     if response:
#                         st.info(
#                             f"Time Taken: {elapsed_time:.2f} seconds", icon="⌚")
#                         json_string = hp.clean_response(response)

#                         if json_string:
#                             try:
#                                 json_data = json.loads(json_string)
#                                 json_data = hp.clean_numeric_values(json_data)

#                                 updated_json_data = DisplayDetails.print_response_from_image(
#                                     json_data)

#                             except json.JSONDecodeError as e:
#                                 st.error(f"Error decoding JSON: {e}")
#                         else:
#                             st.error("Cleaned JSON response is empty.")
#                     else:
#                         st.error("No response received from the Gemini API.")
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# import time
# import json
# import streamlit as st
# from PIL import Image, ImageEnhance, ImageFilter
# from Input import input_value
# import DisplayDetails
# import Helper as hp
# import GeminiIntegration as gi


# def set_dark_theme():
#     """Set custom dark theme for the Streamlit application"""
#     st.markdown("""
#     <style>
#     /* File uploader container styling */
#     .stFileUploader {
#         background-color: black !important;
#         border: 2px solid black !important;
#         border-radius: 10px !important;
#         padding: 15px !important;
#     }

#     .stFileUploader > div {
#         background-color: black !important;
#         border-radius: 8px !important;
#     }

#     .stFileUploader > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div > div {
#         background-color: black !important;
#     }

#     .stFileUploader > div > div > div > input {
#         background-color: black !important;
#         color: white !important;
#         border: 1px solid #333 !important;
#         border-radius: 6px !important;
#     }

#     /* Drag and drop text */
#     .stFileUploader > div > div > div > p {
#         color: #888 !important;
#     }

#     /* Additional dark theme styles */
#     body {
#         background-color: black !important;
#         color: white !important;
#     }

#     .stApp {
#         background-color: black !important;
#     }

#     .stTextInput > div > div > input {
#         background-color: black !important;
#         color: white !important;
#         border: 1px solid #333 !important;
#     }

#     .stButton > button {
#         background-color: rgb(255, 75, 75) !important;
#         color: white !important;
#         border: none;
#     }

#     .stButton > button:hover {
#         background-color: rgb(255, 100, 100) !important;
#     }

#     .stImage {
#         border: 2px solid #333;
#         border-radius: 8px;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# def image_upload():
#     # Apply dark theme
#     set_dark_theme()

#     # Subheader with dark theme color
#     st.markdown("<h2>Upload Receipt Image to Analyse...</h2>",
#                 unsafe_allow_html=True)

#     uploaded_file = st.file_uploader(
#         "Upload a Receipt...", type=["jpg", "jpeg", "png"])
#     image = None

#     if uploaded_file:
#         try:
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_container_width=True)

#         except Exception as e:
#             st.error(f"Error processing the uploaded file: {e}")

#     if st.button("Analyse Uploaded Receipt"):
#         if not uploaded_file:
#             st.error("Please upload an image to proceed.")
#         else:
#             try:
#                 with st.spinner('Processing receipt...'):
#                     enhanced_image = hp.enhance_image(image)

#                     start_time = time.time()
#                     response = gi.get_gemini_response(
#                         input_value, enhanced_image)
#                     elapsed_time = time.time() - start_time

#                     if response:
#                         st.info(
#                             f"Time Taken: {elapsed_time:.2f} seconds", icon="⌚")
#                         json_string = hp.clean_response(response)

#                         if json_string:
#                             try:
#                                 json_data = json.loads(json_string)
#                                 json_data = hp.clean_numeric_values(json_data)

#                                 updated_json_data = DisplayDetails.print_response_from_image(
#                                     json_data)

#                             except json.JSONDecodeError as e:
#                                 st.error(f"Error decoding JSON: {e}")
#                         else:
#                             st.error("Cleaned JSON response is empty.")
#                     else:
#                         st.error("No response received from the Gemini API.")
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
