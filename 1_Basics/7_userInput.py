import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname", max_chars=10)
st.title(fname)
# text input hide password
password = st.text_input("Enter Password", type="password")

# text area
message = st.text_area("Enter Message")
st.write(message)

# numbers
# for float use -> number = st.number_input("Enter Number",1.0,25.0)
number = st.number_input("Enter Number", 1, 25)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My time")

# color picker
color = st.color_picker("select color")
