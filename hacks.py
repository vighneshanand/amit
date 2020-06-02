# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:13:37 2020

@author: amit
"""

import streamlit as st
import pandas as pd

st.title("Enter value")

user_input = st.text_input("label goes here")


DATA_URL = r'C:\Users\amit\Downloads\GRE.xlsx'

df = pd.read_excel(DATA_URL)



if user_input!="":
    val = int(user_input)
    st.dataframe(df[df['Scores']<val])

else :
    st.write("Results will show up here")

  # Same as st.write(df)

 
