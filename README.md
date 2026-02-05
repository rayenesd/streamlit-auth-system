#Streamlit Login & OTP App

A simple Streamlit app for user signup and login with OTP email verification.
The app allows users to:

Create an account (signup)

Login using email and password

Receive an OTP code via email (optional verification)

Built with Python, Streamlit, and smtplib.

Features

Signup page with email, full name, and password

Login page with email and password

OTP code sent to email after login

Uses st.session_state to store user data

Easy navigation between pages

Requirements

Python 3.7+

Streamlit

smtplib (built-in Python library)

Install Streamlit if you don’t have it:

pip install streamlit

Usage

Clone the repository:

git clone https://github.com/yourusername/streamlit-login-otp.git


Navigate to the project folder:

cd streamlit-login-otp


Run the Streamlit app:

streamlit run app.py


Open the link provided in the terminal to view the app in your browser.

How it Works

Signup: Users enter email, full name, and password.

Login: Users enter their email and password.

OTP Email: The app generates a random 5-digit OTP and sends it via email.

Note: For Gmail, you need to use an app password instead of your main password.

Project Structure
streamlit-login-otp/
│
├── app.py          # Main Streamlit app
├── README.md       # This file
└── requirements.txt

License

This project is licensed under the MIT License.

If you want, I can also write a short requirements.txt for this project so anyone can install all dependencies in one command.

Do you want me to do that?

