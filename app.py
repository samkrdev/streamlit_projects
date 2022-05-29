import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd


def main():
    st.title("Welcome to Streamlit!")

    st.write("Our first DataFrame")

    st.write(
    pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
        })
    )

    checkbox_one = st.checkbox("Yes")
    checkbox_two = st.checkbox("No")

    if checkbox_one:
        value = "Yes"
    elif checkbox_two:
        value = "No"
    else:
        value = "No value selected"

    st.write(f"You selected: {value}")
    start_x = st.sidebar.slider("Start X", value= 24, key='sx')
    start_y = st.sidebar.slider("Start Y", value= 332, key='sy')
    finish_x = st.sidebar.slider("Finish X", value= 309, key='fx')
    finish_y = st.sidebar.slider("Finish Y", value= 330, key='fy')


    
if __name__ == "__main__":
    main()
