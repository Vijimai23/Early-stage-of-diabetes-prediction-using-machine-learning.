import streamlit as st

import base64
import numpy as np
import matplotlib.pyplot as plt 
from tkinter.filedialog import askopenfilename

import streamlit as st

import matplotlib.image as mpimg

import streamlit as st
import base64

import pandas as pd
import sqlite3

# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.avif')


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Artificial Intelligence and Machine Learning for Improving Glycemic Control in Diabetes: Best Practices, Pitfalls, and Opportunities"}</h1>', unsafe_allow_html=True)
    
    print()
    print()

    print()

    st.text("                 ")
    st.text("                 ")
    a = " Artificial Intelligence (AI) and Machine Learning (ML) are increasingly pivotal in the realm of healthcare, particularly in optimizing glycemic control for individuals with diabetes. This paper explores best practices, pitfalls, and opportunities associated with the integration of AI and ML in diabetes management. Key practices include the utilization of predictive modeling to anticipate blood glucose levels, personalized treatment recommendations based on patient-specific data, and continuous monitoring through wearable devices and mobile apps. Pitfalls such as data privacy concerns, algorithm bias, and the challenges of integrating AI into clinical workflows are addressed. Opportunities lie in the potential for AI to improve adherence to treatment regimens, enhance patient outcomes through real-time feedback, and facilitate personalized medicine approaches. By examining these facets, this paper aims to guide healthcare practitioners and researchers in navigating the complexities of implementing AI and ML solutions to achieve superior glycemic control in diabetes care."
    
    st.markdown(f'<h1 style="color:#000000;text-align: justify;font-size:20px;font-family:Caveat, sans-serif;">{a}</h1>', unsafe_allow_html=True)

    st.text("                 ")
    st.text("                 ")
    
    st.text("                 ")
    st.text("                 ")
    
    # col1,col2,col3 = st.columns(3)
    
    # with col1:
        
    #     st.image("b1.jpg")

    # with col2:
        
    #     st.image("b2.jpg")

    # with col3:
        
    #     st.image("b3.jpg")



elif navigation()=='reg':
   
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Artificial Intelligence and Machine Learning for Improving Glycemic Control in Diabetes: Best Practices, Pitfalls, and Opportunities"}</h1>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Register Here !!!"}</h1>', unsafe_allow_html=True)
    
    import streamlit as st
    import sqlite3
    import re
    
    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    # Function to create a new user
    def create_user(conn, user):
        sql = ''' INSERT INTO users(name, password, email, phone)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    
    # Function to check if a user already exists
    def user_exists(conn, email):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        if cur.fetchone():
            return True
        return False
    
    # Function to validate email
    def validate_email(email):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.match(pattern, email)
    
    # Function to validate phone number
    def validate_phone(phone):
        pattern = r'^[6-9]\d{9}$'
        return re.match(pattern, phone)
    
    # Main function
    def main():
        # st.title("User Registration")
    
        # Create a database connection
        conn = create_connection("dbs.db")
    
        if conn is not None:
            # Create users table if it doesn't exist
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT NOT NULL UNIQUE,
                         phone TEXT NOT NULL);''')
    
            # User input fields
            name = st.text_input("Enter your name")
            password = st.text_input("Enter your password", type="password")
            confirm_password = st.text_input("Confirm your password", type="password")
            email = st.text_input("Enter your email")
            phone = st.text_input("Enter your phone number")
    
            col1, col2 = st.columns(2)

            with col1:
                    
                aa = st.button("REGISTER")
                
                if aa:
                    
                    if password == confirm_password:
                        if not user_exists(conn, email):
                            if validate_email(email) and validate_phone(phone):
                                user = (name, password, email, phone)
                                create_user(conn, user)
                                st.success("User registered successfully!")
                            else:
                                st.error("Invalid email or phone number!")
                        else:
                            st.error("User with this email already exists!")
                    else:
                        st.error("Passwords do not match!")
                    
                    conn.close()
                    # st.success('Successfully Registered !!!')
                # else:
                    
                    # st.write('Registeration Failed !!!')     
            
            with col2:
                    
                aa = st.button("LOGIN")
                
                if aa:
                    import subprocess
                    subprocess.run(['python','-m','streamlit','run','login.py'])
                    # st.success('Successfully Registered !!!')
    
    
    
  
    if __name__ == '__main__':
        main()



elif navigation()=='model':
    
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Artificial Intelligence and Machine Learning for Improving Glycemic Control in Diabetes: Best Practices, Pitfalls, and Opportunities"}</h1>', unsafe_allow_html=True)
  
    col1,col2,col3 = st.columns(3)
    
    with col2:
        butt = st.button("Go To Training")
      
        if butt:
        
            import subprocess
            subprocess.run(['python','-m','streamlit','run','Prediction.py'])
  
    
  



    
    
    
    
    