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