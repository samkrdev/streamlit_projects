import streamlit as st
import pandas as pd
from memory_profiler import profile

@profile
def main():
    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Home":
        st.subheader("Forms tutorial")

        # Salary Calculator
        # Combine forms + Columns
        with st.form(key="salaryform", clear_on_submit=True):
            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                amount = st.number_input("Hourly rate in $")
            with col2:
                hour_per_week = st.number_input("Hours per week", 1, 120)
            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label="Calculate")
        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hour_per_week]
                df = pd.DataFrame({"hourly": amount, "daily": daily, "weekly": weekly})
                df.astype(int, errors="ignore")
                st.dataframe(df.T)

        # Method 1: context manager Approach (with)
        with st.form(key="form1", clear_on_submit=True):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")

            submit_button = st.form_submit_button(label="Signup")
            # Result can be outside or inside the form
            if submit_button:
                st.success(f"Hello {firstname} you've created an account")

        # Method 2
        form2 = st.form(key="form2", clear_on_submit=True)
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job", ["Dev", "Data Scientist", "Doctor"])
        submit_button2 = form2.form_submit_button("Login")
        if submit_button2:
            st.write(f"{username.upper()}-{jobtype}")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
