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
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success(f'New password: {new_random_password}')
        DataController.userDataController.saveUserData()
        # The developer should securely transfer the new password to the user.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)