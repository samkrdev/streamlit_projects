import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
import pdfplumber
import os

# Load images
@st.cache
def load_images(image_file):
    img = Image.open(image_file)
    return img


def save_uploaded_file(uploadedfile):
    with open(os.path.join("data/uploaded_files", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.write(f"{uploadedfile.name} saved")


def main():
    st.title("File upload Turorial")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            st.write(type(image_file))
            # st.write(dir(image_file))
            file_details = {
                "filename": image_file.name,
                "filetype": image_file.type,
                "filesize": image_file.size,
            }
            st.write(file_details)
            st.image(load_images(image_file), width=250)
            # Saving file
            with open(os.path.join("data/uploaded_files", image_file.name), "wb") as f:
                f.write(image_file.getbuffer())
                st.write(f"{image_file.name} saved")
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            st.write(type(data_file))
            file_details = {
                "filename": data_file.name,
                "filetype": data_file.type,
                "filesize": data_file.size,
            }
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            save_uploaded_file(data_file)
    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if docx_file is not None:

                file_details = {
                    "filename": docx_file.name,
                    "filetype": docx_file.type,
                    "filesize": docx_file.size,
                }
                st.write(file_details)
                if docx_file.type == "text/plain":
                    # Read as bytes
                    raw_text = docx_file.read()
                    # Read as string
                    text = str(raw_text, "utf-8")
                    st.write(text)
                elif docx_file.type == "application/pdf":
                    # With pdfplumber

                    try:
                        with pdfplumber.open(docx_file) as pdf:
                            st.title("With PDF plumber")
                            pages = pdf.pages[0]
                            st.write(pages.extract_text())
                    except:
                        st.write("None")

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
