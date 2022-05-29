import streamlit as st


def main():

    # Superfunction
    st.write("Normal text")
    st.write("## This is a text")
    st.write(1 + 2)
    st.write(dir(st))
    # Help info
    st.help(print)
    st.help(range)


if __name__ == "__main__":
    main()
