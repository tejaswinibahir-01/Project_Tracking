import pickle
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth

def app():
    # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
    st.markdown("""___""")
    st.title("User-Profile")

    # --- USER AUTHENTICATION ---
    names = ["Teju", "Shreya"]
    usernames = ["TAB", "SRG"]

    # load hashed passwords
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"sales_dashboard", "2002",cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")
    Manager = "Manager"
    Employee = "Employee"
    Designantion = st.multiselect("select the designantion:",[Manager,Employee])

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")


    if authentication_status:
        # ---- READ EXCEL ----
        st.header(f"Welcome {name}")
        st.subheader(f"Designation: {Designantion}")
        authenticator.logout("Logout", "main")

    st.markdown("""___""")
