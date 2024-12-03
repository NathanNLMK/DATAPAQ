import streamlit as st 



def createPage():
    st.empty()
    st.write("Home Page")
    if st.session_state['authentication_status'] is None:
        st.write("il faut d'abord vous login")
    else :
        st.write("bienvenue")
    return True