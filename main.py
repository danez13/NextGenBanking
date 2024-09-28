import streamlit as st
import streamlit_authenticator as stauth
import DataController
st.set_page_config(
    page_title="Login"
)
authenticator = stauth.Authenticate(
    DataController.userDataController.config['credentials'],
    DataController.userDataController.config['cookie']['name'],
    DataController.userDataController.config['cookie']['key'],
    DataController.userDataController.config['cookie']['expiry_days'],
    DataController.userDataController.config['pre-authorized']
)
name, authStatus, username = authenticator.login("main",1,3)
if st.button("create account",):
    st.switch_page("pages/register.py")
if st.session_state['authentication_status']:
    st.empty()
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.info('Please enter your username and password')