import streamlit as st
import streamlit.components as stc
#Utils
import base64
import time
import pandas as pd
timestr = time.strftime("%Y%m%d-%H%M%S")

class FileDownloader(object):
    """docstring for FileDownloader
    >>> download = FileDownloader(data,filename,file_ext).download()

    """
    def __init__(self, data,filename='myfile',file_ext='txt'):
        super(FileDownloader, self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = "{}_{}_.{}".format(self.filename,timestr,self.file_ext)
        st.markdown("#### Download File ###")
        href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href,unsafe_allow_html=True)
def main():
    menu = ["Home","CSV","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice =='Home':
        st.subheader("Home")
        my_text = st.text_area("Your Message")
        if st.button("Save"):
            st.write(my_text)
            download = FileDownloader(my_text).download()

    elif choice == "CSV":
        df = pd.read_csv("data/iris.csv")
        st.dataframe(df)
        FileDownloader(df.to_csv(),file_ext='csv').download()
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()