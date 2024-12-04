import streamlit as st 
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def load_config():
    with open('config.yaml') as file:
        template = file.read()
        config_string = template.format(
            COOKIE_KEY=st.secrets["COOKIE_KEY"],
            USER1_PASSWORD=st.secrets["USER1_PASSWORD"],
            USER2_PASSWORD=st.secrets["USER2_PASSWORD"],
            USER3_PASSWORD=st.secrets["USER3_PASSWORD"]
        )
        config = yaml.safe_load(config_string)
    return config


def createPage():
    st.empty()
    st.write("Login page")
    
    config = load_config()
    
    #print("Configuration loaded:",config)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        auto_hash=False
    )
    try:
        authenticator.login()
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")


    if st.session_state['authentication_status']:
        st.success(f"Bienvenue {st.session_state['name']}")
        
        authenticator.logout()
    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')
    return True
