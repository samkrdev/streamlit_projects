import streamlit as st
import pandas as pd

# Display Data
df=pd.read_csv("data/iris.csv")

# Method 1

st.dataframe(df,500,300 ) # df,width,height

# You can also add a color style from pandas

st.dataframe(df.style.highlight_max(axis=0))

# Method 2: Static Table
st.table(df.head())

# Method 3: using Super function st.write
st.write(df.head())

# Display Json
st.json({'data':'name'})

# Displa code
mycode = """ 
def sayhello():
    print("Hello World")
"""
st.code(mycode,language='python')
