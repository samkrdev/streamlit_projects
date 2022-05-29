import streamlit as st

# Method 1
st.set_page_config(
    page_title="hello", page_icon=":fire:", layout="wide", initial_sidebar_state="auto"
)

# Method 2
# PAGE_CONFIG = dict(page_title='hello',page_icon=':fire:',layout='wide',initial_sidebar_state='auto')
# st.set_page_config(**PAGE_CONFIG)
def main():
    st.title("Hello World")
    st.sidebar.success("Menu")


if __name__ == "__main__":
    main()
