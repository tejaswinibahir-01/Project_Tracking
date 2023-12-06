import streamlit as st

from streamlit_option_menu import option_menu

import login,Homepage,Projects,Report


st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():

        app = option_menu(

            menu_title=None,
            options=['Home','Projects','Report','Account'],
            icons=['house-fill','book','info-circle-fill','person-circle'],
            orientation='horizontal',

            default_index=1,
            styles={
                    "container": { "position":"top","background":"#F0F2F6", "width":"100%" ,"height":"90px"},
                    "icon": { "font-size": "18px",},
                    "nav-link": {"color": "black", "font-size": "15px", "text-align": "center", "margin": "20px",
                                 },
                    "nav-link-selected": {"width":"70%","color": "white"},


                     }
    #"--hover-color": "blue","nav-link-selected": {"background-color": "#02ab21"}
        )
        if app == "Account":
            login.app()

        if app == "Home":
            Homepage.app()

        if app == "Projects":
            Projects.app()

        if app == "Report":
            Report.app()


    run()

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
#st.markdown(hide_st_style, unsafe_allow_html=True)