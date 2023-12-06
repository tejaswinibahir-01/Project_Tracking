import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from PIL import Image
from login import app
import streamlit_authenticator as stauth

def app():


    excel_file = "Mastersheet_1.xlsx"
    sheet_name = 'Mastersheet_1'
    df = pd.read_excel(excel_file)
    df.dropna(inplace=True)
    st.markdown("""---""")
    exp1=st.expander("See Pictorial Report")
    exp1.header("Project Report")
    with exp1:
        bar_chart= px.bar(df, x="Project_Id",y="Employee_Id",color='Task_Status',barmode='group')
        st.plotly_chart(bar_chart)

    exp2 = st.expander("See Verbal Report")
    exp2.header("Project Report")

    with exp2:
        df2 = pd.read_excel(excel_file, header=[0, 1])
        grouped_df = df.groupby(['Project_Id', 'Task_Status']).size().reset_index(name='Count')
        pivot_df = grouped_df.pivot(index='Project_Id', columns='Task_Status', values='Count').fillna(0)

        # Filter relevant columns
        filtered_df = df.loc[:, ['Project_Id', 'Task_Id', 'Task_Name', 'Task_Status']]

        # Iterate through unique projects
        for project_id in filtered_df['Project_Id'].unique():
            st.subheader(f"For Project: {project_id}")

            # Filter data for the current project
            project_data = filtered_df[filtered_df['Project_Id'] == project_id]

            # Print task information for the current project
            for _, row in project_data.iterrows():
                task_id = row[('Task_Id')]
                task_name = row[('Task_Name')]
                task_status = row[('Task_Status')]

                st.write(f"**Task ID:** {task_id}, **Task Name:** {task_name}, **Task Status:** {task_status}")

        for project_id, group in df.groupby('Project_Id'):
            st.write(f"Project: {project_id}")
            task_counts = group['Task_Status'].value_counts()

            completed = task_counts.get('COMPLETED', 0)
            inprocess = task_counts.get('INPROCESS', 0)
            delayed = task_counts.get('DELAYED', 0)

            st.write(f"Completed tasks: {completed}")
            st.write(f"Inprocess tasks: {inprocess}")
            st.write(f"Delayed tasks: {delayed}")
            st.empty()





    st.markdown("""___""")