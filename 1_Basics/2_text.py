import streamlit as st

def main():
    # simple text
    st.text("This is a test text")
    # header
    st.header("This is a header")
    # Subheader
    st.subheader("This is a subheader")
    # title
    st.title("This is a title")
    # Markdown
    st.markdown("""
    ```python
    names = ['sam','amy']
    print("Hello World")
    ```
    """)

    # Displaying colored text/

if __name__ == '__main__':
    main()