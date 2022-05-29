import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    

    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Home':
        st.title("Main App")
        st.subheader("Home")
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()
    else:
        st.subheader('About')


if __name__ == '__main__':
    main()