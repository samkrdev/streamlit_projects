import streamlit as st
import pandas as pd
from db_fxns import *
import plotly.express as px

def main():
    st.set_page_config(layout="wide")
    st.title("TODO App")
    
    menu = ["Create", "Read", "Update", "Delete", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Create":
        st.subheader("Add Items")

        # layout
        col1, col2 = st.columns(2)
        with col1:
            task = st.text_area("Task To Do")
        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            add_data(task,task_status,task_due_date)
            st.success(f"Successfully Added Data:{task}")

    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
        with st.expander('View All Data'):
            st.dataframe(df)

        with st.expander('Task Status'):
            task_df = df['Status'].value_counts().to_frame().reset_index()
            st.dataframe(task_df)
            pl = px.pie(task_df,names='index',values='Status')
            st.plotly_chart(pl)

    elif choice == "Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
        with st.expander("Current Data"):
            st.dataframe(df)
        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Task",list_of_tasks)
        task_result = get_task(selected_task)
        st.write(task_result)
        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]

            col1,col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do",task)

            with col2:
                values = ["ToDo","Doing","Done"]
                default_ix = values.index(task_status)
                new_task_status = st.selectbox("Status",values,index=default_ix)
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
                st.success("Updated ::{} ::To {}".format(task,new_task))

            with st.expander("View Updated Data"):
                result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)
    elif choice == "Delete":
        st.subheader("Delete Item")
        with st.expander("View Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name =  st.selectbox("Select Task",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Updated Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
