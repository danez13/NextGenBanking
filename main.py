import streamlit as st
import streamlit_authenticator as stauth
import DataController
import random
st.set_page_config(
    page_title="Login"
)
def makeTransaction(oneline,usedpin,usedchip,repeat,purchaseprice,location):
    st.checkbox("online purchase?")
    st.checkbox("was a pin used?")
    st.checkbox("was the chip used?")
    st.checkbox("repeat retailer?")
    st.number_input("How much did you pay")

authenticator = stauth.Authenticate(
    DataController.userDataController.config['credentials'],
    DataController.userDataController.config['cookie']['name'],
    DataController.userDataController.config['cookie']['key'],
    DataController.userDataController.config['cookie']['expiry_days'],
    DataController.userDataController.config['pre-authorized']
)
name, authStatus, username = authenticator.login("main",1,3)
location = False
main = st.empty()
with main.container():
    col1, col2 = st.columns(2)
    with col1:
        if col1.button("create account"): 
            st.switch_page("pages/register.py")
    with col2:
        if col2.button("forgot password"):
            st.switch_page("pages/forgotpass.py")

if st.session_state['authentication_status']:
    body = main.empty()
    cont1,cont2=body.columns(2)
    col1, col2,col3 = body.columns([1,1,1])
    with cont1:
        with col1:
            col1.write(f'Welcome *{st.session_state["name"]}*')
        with col2:
            updateDetails = col2.button("update details")
        with col3:
            authenticator.logout()
    cont2 = st.container()
    with cont2:
        with cont2:
            if updateDetails:
                if st.session_state['authentication_status']:
                    try:
                        if authenticator.update_user_details(st.session_state['username']):
                            cont2.success('Entries updated successfully')
                    except Exception as e:
                        cont2.error(e)
            if cont2.button("make Transaction"):
                pass

elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.info('Please enter your username and password')