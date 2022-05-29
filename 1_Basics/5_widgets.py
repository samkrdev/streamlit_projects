import streamlit as st

# Working with Buttons
name = "Sam"

if st.button("submit",key="nameUpperSubmit"):
    st.write(f"Name:{name.upper()}")

if st.button("submit",key="nameLowerSubmit"):
    st.write(f"Name:{name.lower()}")

# Working with Radiobuttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
    st.success("You are active")
elif status == 'Inactive':
    st.warning("Inactive")

# Working with Checkbox
if st.checkbox("Show/Hide"):
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")

# Select/Multiple select
my_lang = [None,'Python',"Julia","Go","Rust"]

choice = st.selectbox("Language",my_lang)
if not choice == None:
    st.write(f"You selected {choice}")

# Multiple Selection
spoken_lang = ("English","French","Spanish","Twi")
my_Spoken_lang = st.multiselect("Spoken Lang",spoken_lang)
st.write(my_Spoken_lang)

# Slider
# Numbers (int,float,dates)
age = st.slider("age",1,100,value=(20,30))
st.write(age)
age1 = st.slider("age",1,100)
st.write(age1)

# Select Slider
color = st.select_slider("Choose Color",options=["yellow","red","blue","black","white"],value=("yellow","red"))
st.write(color)