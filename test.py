import streamlit as st
import smtplib
from email.message import EmailMessage
import random

# activate server 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'rsaoudi461@gmail.com'
server.login(from_mail, 'hfdn zqoa pboq upnc')

# first page 
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'reg_email' not in st.session_state:
    st.session_state.reg_email = ''
    st.session_state.reg_password = ''
    st.session_state.reg_name = ''

if 'otp' not in st.session_state:
    st.session_state.otp = ''
if 'otp_verified' not in st.session_state:
    st.session_state.otp_verified = False

if st.session_state.page == "home":
    st.title("Welcome")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Sign-up"):
            st.session_state.page = "signup"

        if st.button("Login"):
            st.session_state.page = "login"

# sign up page
elif st.session_state.page == "signup": 
    with st.form("signup page"):
        reg_email = st.text_input("Enter your email")
        reg_name = st.text_input("Enter your full name")
        reg_password = st.text_input("Enter your password", type="password")

        submitted = st.form_submit_button("Create account")
    if submitted:
        st.session_state.reg_email = reg_email
        st.session_state.reg_password = reg_password
        st.session_state.reg_name = reg_name
        st.success("Account created! Go back to Home to login.")
    if st.button("Go to Login"):
        st.session_state.page = "login"
elif st.session_state.page == "login": 
    with st.form("login page"):
        log_email = st.text_input("Enter your email: ")
        log_password = st.text_input("Enter your password", type="password")

        enter = st.form_submit_button("connect")
        
        if enter :
            if log_email == st.session_state.reg_email and log_password == st.session_state.reg_password:
                st.text("email and password correct")
                otp_code = random.randrange(10000, 99999)
                st.session_state.otp = otp_code
                # send otp code
                msg = EmailMessage()
                msg['subject'] = "OTP verification"
                msg['from'] = from_mail
                msg['to'] = log_email
                msg.set_content("Your OTP code: "+ str(otp_code))
                server.send_message(msg)

                st.text("Email sent")
                st.session_state.page = "otp"
            else:
                st.error("Email or password incorrect")
elif st.session_state.page == "otp":
    with st.form("otp_form"):
        entered_otp = st.text_input("Enter the OTP sent to your email")
        verify = st.form_submit_button("Verify OTP")

        if verify:
            if entered_otp == str(st.session_state.otp):
                st.success("OTP verified! You are now logged in.")
                st.session_state.otp_verified = True
            else:
                st.error("Incorrect OTP. Try again.")