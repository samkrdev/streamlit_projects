import streamlit as st

#utils
import logging

#Terminal
# FORMAT
LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d-%(message)s"
# create a logger
# logging.basicConfig(level=logging.DEBUG,format=LOGS_FORMAT)
# logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("activity.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(asctime)s:%(levelname)s:%(message)s'))
    logger.addHandler(file_handler)

def main():
    st.title("Add logs to all apps")
    st.text("Track all activities/pages of apps")

    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Home':
        st.title("Main App")
        st.subheader("Home")
        logger.info("Home Section")
    elif choice == 'EDA':
        st.subheader("EDA")
        logger.info("EDA")
    elif choice == 'ML':
        st.subheader("ML")
        logger.info("ML")
        st.subheader("Analytics")
        logger.info("Analytics Section")
    else:
        st.subheader('About')
        logger.info("About")


if __name__ == '__main__':
    main()