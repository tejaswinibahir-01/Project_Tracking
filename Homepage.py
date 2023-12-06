import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from PIL import Image
from login import app
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

def app():


    excel_file ="Mastersheet_1.xlsx"
    sheet_name = 'Mastersheet_1'
    st.markdown("""---""")
    left, middle, right = st.columns(3)
    with middle:
        st.header("Project-Details-2023")

    st.markdown("""---""")
    l3, l2, l, m, r, r2, r3 = st.columns(7)
    left_column1,left_column,middle_column,right_column,right_column1 = st.columns(5)
    with m:
        st.header(" ")
        st.write("Visual Report")

    with left_column:
        df = pd.read_excel(excel_file)
        df.dropna(inplace=True)
        pie_chart = px.pie(df, names='Task_Status')
        st.plotly_chart(pie_chart,theme="streamlit")

    st.markdown("""---""")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    st.subheader(":star:Write Note For Self")
    my_input = st.text_input( st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered: ", my_input)
    st.markdown("""---""")





    # --- USER AUTHENTICATION ---
    names = ["Teju", "Shreya"]
    usernames = ["TAB", "SRG"]

    # load hashed passwords
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard", "2002",
                                        cookie_expiry_days=30)
    with st.sidebar:

        st.markdown("""___""")
        st.title("Profile")
        st.markdown("""___""")
        name, authentication_status, username = authenticator.login("Login", "main")

        if authentication_status == False:
            st.error("Username/password is incorrect")

        if authentication_status == None:
            st.warning("Please enter your username and password")

        if authentication_status:
            st.header(f"Welcome {name}")
            st.subheader("Designation: Manager")
            authenticator.logout("Logout", "sidebar")



