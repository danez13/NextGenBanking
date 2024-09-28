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
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False,captcha=True,clear_on_submit=True)
    DataController.userDataController.config['credentials']["usernames"][username_of_registered_user]
    if email_of_registered_user:
        st.success('User registered successfully')
except Exception as e:
    # st.error(e)
    pass
st.info(DataController.userDataController.config)