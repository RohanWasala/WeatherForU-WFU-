import Firebase_configkey
import pyrebase
import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt

owm = pyowm.OWM('606ba0a989dbd4bd42c1bddc9139ebe2')
mgr = owm.weather_manager()

# st.title("5 Day Weather Forcast")
# st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")
# place = st.text_input("Name Of The City:", "")
# if place==None:
#     st.write("Input a city!")
# unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))
# g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))

#Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Our Weather app")

#Authentication
choice = st.sidebar.selectbox('login/SignUp',['Login','SignUp'])
email = st.sidebar.text_input("Please enter your email addresss")
password = st.sidebar.text_input("Please enter your password")

if choice == 'SignUp':
    username = st.sidebar.text_input('Please enter your Username', value ='Default')
    submit = st.sidebar.button("Create my account")
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created successfully!')
        st.bolloons()
