from distutils.command.upload import upload
import streamlit as st

from PIL import Image
import os


def load_image(imagefile):
    img = Image.open(imagefile)
    return img


def save_uploaded_file(uploadedfile):
    with open(os.path.join("data/uploaded_files", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.write(f"{uploadedfile.name} saved")


def main():
    st.title("Multiple file uploads app")

    menu = ["home", "about"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "home":
        st.subheader("Upload Multiple files")
        uploadfiles = st.file_uploader(
            "Upload Multiple images",
            type=["png", "jpeg", "jpg"],
            accept_multiple_files=True,
        )
        if uploadfiles is not None:
            for file in uploadfiles:
                st.write(file.name)
                st.image(load_image(file))
                save_uploaded_file(file)

    else:
        st.subheader("About app")


if __name__ == "__main__":
    main()
