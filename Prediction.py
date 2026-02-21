# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 

import streamlit as st
import base64

 # ------------ TITLE 

st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Artificial Intelligence and Machine Learning for Improving Glycemic Control in Diabetes: Best Practices, Pitfalls, and Opportunities"}</h1>', unsafe_allow_html=True)


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

# ===-------------------------= INPUT DATA -------------------- 


# filenamee = st.file_uploader("Choose a Dataset", ['csv'])

# if filenamee is None:
    
#     st.text("Please Upload Dataset")

# else:

    
import pickle
with open('model.pickle', 'rb') as f:
      rf=pickle.load(f)




# ================== PREDICTION  ====================

# st.write("-----------------------------------")
# st.write("          Prediction               ")
st.write("-----------------------------------")

st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{" Prediction "}</h1>', unsafe_allow_html=True)


inpp1 = st.text_input("Enter Gender (0 - Female & 1 - Male) = ")


inpp2 = st.text_input("Enter Age  = ")


inpp3 = st.text_input("Enter Hypertension (0 - No  & 1 - Yes) = ")


inpp4 = st.text_input("Enter Heart Disease (0 - No  & 1 - Yes) = ")    


inpp5 = st.text_input("Enter Smoking History (0 - Current , 1- Ever, 2- Former , 3- Never , 4 - Not Current , 5 - No Info )= ")


inpp6 = st.text_input("Enter BMI  = ")


inpp7 = st.text_input("Enter HbA1c Level = ")


inpp8 = st.text_input("Enter Blood Glucose Level  = ")        



butt = st.button("PREDICT")

if butt:

    final_inp = np.array([int(inpp1), int(inpp2), int(inpp3), int(inpp4),int(inpp5),float(inpp6),float(inpp7),int(inpp8)]).reshape(1, -1)
    
    predicted_data = rf.predict(final_inp)
    
    
    if predicted_data == 0:
        st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = Affected By Diabetes"}</h1>', unsafe_allow_html=True)

    
    elif predicted_data == 1:
        st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = Not Affected By Diabetes "}</h1>', unsafe_allow_html=True)


        
  
        print("---------------------------------------------------------------")
        st.write("------------------------------------------------------------")

        #pie graph

    
    
    