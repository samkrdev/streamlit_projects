import streamlit as st
import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;font-size:{}px">
    <h1 style="color:white;text-align:center;">Streamlit is Awesome </h1>
    <h1 style="color:white;text-align:center;">Session State is Here!! </h1>
    </div>
    """
def main():
    st.title("Sessions")

    menu = ["Home", "Custom_settings", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home Page")
        # Without session
        st.info("Without Session State")
        counter_without_state = 0
        st.write("Initial Value", counter_without_state)
        increment = st.button("Increment Without State")
        if increment:
            counter_without_state += 1
        st.write("Counts without session",counter_without_state)

        # With session
        st.info("With session state")
        st.write(st.session_state)
        if 'counter_one' not in st.session_state:
            st.session_state.counter_one = 0
        if 'counter_two' not in st.session_state:
            st.session_state.counter_two = 0
        increment = st.button("Increment by one")
        if increment:
            st.session_state.counter_one += 1
        # Result of update
        st.write("Counts[with session state]",st.session_state.counter_one)

        col1,col2 = st.columns(2)
        with col1:
            increment = st.button("Increment by One")
            if increment:
                st.session_state.counter_two += 1

        with col2:
            decrement = st.button("Decrement by One")
            if decrement:
                st.session_state.counter_two -= 1

        st.write("Counts with session state",st.session_state.counter_two)
            
    elif choice == "Custom_settings":
        st.subheader("App Custom Settings")

        # Define and Initialize State
        if 'fontsize' not in st.session_state:
            st.session_state.fontsize = 12


        f1,f2 = st.columns(2)

        with f1:
            # Create a button for fxn/cb fxn
            font_increment = st.button('Increase Font')
            if font_increment:
                st.session_state.fontsize += 5


        with f2:
            # Create a button for fxn/cb fxn
            font_decrement = st.button('Decrease Font')
            if font_decrement:
                st.session_state.fontsize -= 5	


        # Results
        st.write("Current Font Size",st.session_state.fontsize)
        stc.html(HTML_BANNER.format(st.session_state.fontsize))


if __name__ == "__main__":
    main()
