import streamlit as st
from streamlit_option_menu import option_menu
import Home
import ScanRecipt
import About


st.set_page_config(
    page_title="FinTrack - Simplify Your Finances",
    page_icon="https://github.com/deringirish/DevOpsTesing/blob/main/confluence.jpeg?raw=true",
    layout="wide",
    initial_sidebar_state="collapsed"

)


def streamlit_menu():

    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Contact"],
        icons=["house", "receipt", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    return selected


selected = streamlit_menu()

if selected == "Home":
    Home.landing_page()
if selected == "Projects":
    ScanRecipt.ScanReceipt()
if selected == "Contact":
    # st.title(f"You have selected {selected}")
    # Contact.contact_page()
    About.about_us_page()
