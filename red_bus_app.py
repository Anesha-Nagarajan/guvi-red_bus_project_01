import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to Red Bus App!') 
st.markdown(''':bus:''')
# st.selectbox("Anesha","Sreram","Koushik","Nagarajan","Sumathi")

st.button('Submit')

df = pd.read_csv("C:/Users/nagar/Documents/Guvi Projects/Red_bus_project_01_files/Red_bus_df.csv")

st.dataframe(df)

st.video("C:/Users/nagar/Documents/Guvi Projects/bus_video.mp4")