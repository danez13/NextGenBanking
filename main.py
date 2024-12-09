import streamlit as st
import streamlit_authenticator as stauth
import DataController
import random
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
main = st.empty()
if st.session_state['authentication_status'] is None:
    with main.container():
        login_form_container = st.container()
        with login_form_container:
            name, authStatus, username = authenticator.login("main",1,3)

        button_container = st.container()
        with button_container:
            col1, col2 = st.columns(2)
            with col1:
                if col1.button("create account"): 
                    st.switch_page("pages/register.py")
            with col2:
                if col2.button("forgot password"):
                    st.switch_page("pages/forgotpass.py")
        if st.session_state['authentication_status'] is False:
            st.error('Username/password is incorrect')
        elif st.session_state['authentication_status'] is True:
            st.rerun()
        else:
            st.info('Please enter your username and password')

elif st.session_state['authentication_status']:
    st.session_state["account_settings"] = False
    body = main.empty()
    cont1,cont2=body.columns(2)
    col1, col2,col3 = body.columns([1,1,1])
    with cont1:
        with col1:
            col1.write(f'Welcome *{st.session_state["name"]}*')
        with col2:
            account = col2.button("account settings")
            if account:
                st.session_state["account_settings"] = True
    cont2 = st.container()
    with cont2:
        if st.session_state["account_settings"]:
            st.session_state["update_Details"] = False
            col1, col2, col3 = st.columns(3)
            with col1:
                updateDetails = col2.button("update details")
                if updateDetails == True:
                    st.session_state["update_Details"] = True
            with col2:
                authenticator.logout()
    cont3 = st.container()
    with cont3:
        if st.session_state["update_Details"]:
            try:
                if authenticator.update_user_details(st.session_state['username']):
                    cont2.success('Entries updated successfully')
            except Exception as e:
                cont2.error(e)