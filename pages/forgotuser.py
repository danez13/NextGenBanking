import streamlit as st
import streamlit_authenticator as stauth
import DataController

authenticator = stauth.Authenticate(
    DataController.userDataController.config['credentials'],
    DataController.userDataController.config['cookie']['name'],
    DataController.userDataController.config['cookie']['key'],
    DataController.userDataController.config['cookie']['expiry_days'],
    DataController.userDataController.config['pre-authorized']
)

try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username to be sent securely')
        st.success(f'New password: {username_of_forgotten_username}')
    elif username_of_forgotten_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)