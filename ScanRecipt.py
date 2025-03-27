import streamlit as st
import ImageUpload
import ManualEntry


def ScanReceipt():

    st.header("FinTrack-Simplifying Personal Finance")

    image_upload,  manual_entry = st.tabs(
        ["🖼️ Image Upload", "📝 Manual Entry"])

    with image_upload:
        ImageUpload.image_upload()

    with manual_entry:
        ManualEntry.manual_entry()


# import streamlit as st
# import ImageUpload
# import ManualEntry


# def ScanReceipt():
#     st.header("Receipt Scanner Application")

#     image_upload, manual_entry = st.tabs(
#         ["🖼️ Image Upload", "📝 Manual Entry"])

#     with image_upload:
#         ImageUpload.image_upload()

#     with manual_entry:
#         ManualEntry.manual_entry()


# import streamlit as st
# import ImageUpload
# import ManualEntry


# def set_dark_theme():
#     """Set custom dark theme for the Streamlit application"""
#     st.markdown("""
#     <style>
#     /* Dark theme base styles */
#     body {
#         color: #e0e0e0;
#         background-color: #121212;
#     }

#     /* Streamlit specific overrides */
#     .stApp {
#         background-color: #121212;
#     }

#     /* Header styling */
#     h1, h2, h3, h4, h5, h6 {
#         color: rgb(255, 75, 75) !important;
#     }

#     /* Tab styling */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: #1e1e1e;
#         border-radius: 8px;
#     }

#     .stTabs [data-baseweb="tab"] {
#         color: #a0a0a0;
#         background-color: #1e1e1e;
#         transition: all 0.3s ease;
#     }

#     .stTabs [data-baseweb="tab"]:hover {
#         color: rgb(255, 75, 75);
#         background-color: #2a2a2a;
#     }

#     .stTabs [data-baseweb="tab"][data-selected="true"] {
#         color: rgb(255, 75, 75);
#         background-color: #2a2a2a;
#         border-bottom: 2px solid rgb(255, 75, 75);
#     }

#     /* Input and file uploader styling */
#     .stTextInput > div > div > input {
#         background-color: #2a2a2a;
#         color: #e0e0e0;
#         border: 1px solid #3a3a3a;
#     }

#     .stFileUploader > div > div > div > input {
#         background-color: #2a2a2a;
#         color: #e0e0e0;
#     }

#     /* Button styling */
#     .stButton > button {
#         background-color: rgb(255, 75, 75);
#         color: white;
#         border: none;
#         transition: all 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: rgb(255, 100, 100);
#         transform: scale(1.05);
#     }
#     </style>
#     """, unsafe_allow_html=True)


# def ScanReceipt():
#     # Apply dark theme
#     set_dark_theme()

#     # Header with dark theme color
#     st.markdown("<h1 style='text-align: center;'>Receipt Scanner Application</h1>",
#                 unsafe_allow_html=True)

#     # Create tabs with dark theme
#     image_upload, manual_entry = st.tabs(
#         ["🖼️ Image Upload", "📝 Manual Entry"])

#     with image_upload:
#         ImageUpload.image_upload()

#     with manual_entry:
#         ManualEntry.manual_entry()

# import streamlit as st
# import ImageUpload
# import ManualEntry


# def set_dark_theme():
#     """Set custom dark theme for the Streamlit application"""
#     st.markdown("""
#     <style>
#     /* Dark theme base styles */
#     body {
#         color: white !important;
#         background-color: #121212;
#     }

#     /* Streamlit specific overrides */
#     .stApp {
#         background-color: #121212;
#         color: white !important;
#     }

#     /* Ensure all text is white */
#     * {
#         color: white !important;
#     }

#     /* Header styling */
#     h1, h2, h3, h4, h5, h6 {
#         color: rgb(255, 75, 75) !important;
#     }

#     /* Tab styling */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: #1e1e1e;
#         border-radius: 8px;
#     }

#     .stTabs [data-baseweb="tab"] {
#         color: white !important;
#         background-color: #1e1e1e;
#         transition: all 0.3s ease;
#     }

#     .stTabs [data-baseweb="tab"]:hover {
#         color: rgb(255, 75, 75) !important;
#         background-color: #2a2a2a;
#     }

#     .stTabs [data-baseweb="tab"][data-selected="true"] {
#         color: rgb(255, 75, 75) !important;
#         background-color: #2a2a2a;
#         border-bottom: 2px solid rgb(255, 75, 75);
#     }

#     /* Input and file uploader styling */
#     .stTextInput > div > div > input {
#         background-color: #2a2a2a;
#         color: white !important;
#         border: 1px solid #3a3a3a;
#     }

#     .stFileUploader > div > div > div > input {
#         background-color: #2a2a2a;
#         color: white !important;
#     }

#     /* Button styling */
#     .stButton > button {
#         background-color: rgb(255, 75, 75);
#         color: white !important;
#         border: none;
#         transition: all 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: rgb(255, 100, 100);
#         transform: scale(1.05);
#     }
#     </style>
#     """, unsafe_allow_html=True)


# def ScanReceipt():
#     # Apply dark theme
#     set_dark_theme()

#     # Header with dark theme color
#     st.markdown("<h1 style='text-align: center;'>Receipt Scanner Application</h1>",
#                 unsafe_allow_html=True)

#     # Create tabs with dark theme
#     image_upload, manual_entry = st.tabs(
#         ["🖼️ Image Upload", "📝 Manual Entry"])

#     with image_upload:
#         ImageUpload.image_upload()

#     with manual_entry:
#         ManualEntry.manual_entry()


# import streamlit as st
# import ImageUpload
# import ManualEntry


# def set_dark_theme():
#     """Set custom dark theme for the Streamlit application"""
#     st.markdown("""
#     <style>
#     /* Dark theme base styles */
#     body {
#         color: white !important;
#         background-color: black;
#     }

#     /* Streamlit specific overrides */
#     .stApp {
#         background-color: black;
#         color: white !important;
#     }

#     /* Ensure all text is white */
#     * {
#         color: white !important;
#     }

#     /* Header styling */
#     h1, h2, h3, h4, h5, h6 {
#         color: rgb(255, 75, 75) !important;
#     }

#     /* Tab styling */
#     .stTabs [data-baseweb="tab-list"] {
#         background-color: #1e1e1e;
#         border-radius: 8px;
#     }

#     .stTabs [data-baseweb="tab"] {
#         color: white !important;
#         background-color: #1e1e1e;
#         transition: all 0.3s ease;
#     }

#     .stTabs [data-baseweb="tab"]:hover {
#         color: rgb(255, 75, 75) !important;
#         background-color: #2a2a2a;
#     }

#     .stTabs [data-baseweb="tab"][data-selected="true"] {
#         color: rgb(255, 75, 75) !important;
#         background-color: #2a2a2a;
#         border-bottom: 2px solid rgb(255, 75, 75);
#     }

#     /* Input and file uploader styling */
#     .stTextInput > div > div > input {
#         background-color: black;
#         color: white !important;
#         border: 1px solid #3a3a3a;
#     }

#     .stFileUploader > div > div > div > input {
#         background-color: black;
#         color: white !important;
#     }

#     /* Button styling */
#     .stButton > button {
#         background-color: rgb(255, 75, 75);
#         color: white !important;
#         border: none;
#         transition: all 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: rgb(255, 100, 100);
#         transform: scale(1.05);
#     }

#     /* Expander styling */
#     .stExpander {
#         border: 1px solid #3a3a3a;
#         background-color: black;
#     }

#     .stExpander > div > div {
#         background-color: black;
#     }

#     /* Selectbox styling */
#     .stSelectbox > div > div {
#         background-color: black;
#         color: white !important;
#         border: 1px solid #3a3a3a;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# def ScanReceipt():
#     # Apply dark theme
#     set_dark_theme()

#     # Header with dark theme color
#     st.markdown("<h1 style='text-align: center;'>Receipt Scanner Application</h1>",
#                 unsafe_allow_html=True)

#     # Create tabs with dark theme
#     image_upload, manual_entry = st.tabs(
#         ["🖼️ Image Upload", "📝 Manual Entry"])

#     with image_upload:
#         ImageUpload.image_upload()

#     with manual_entry:
#         ManualEntry.manual_entry()
