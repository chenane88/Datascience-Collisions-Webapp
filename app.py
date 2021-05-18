import streamlit as st
import pandas as pd
import numpy as np


DATA_URL = {
    "C:/Users/BRADLEY/Documents/GitHub/Data Science Collisions WebApp/Motor_Vehicle_Collisions_-_Crashes.csv"
}

st.title("Motor Vehicle Collision in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motor vehicle collision in NYC 🗽💥🚗")

@st.cache(persist=True)
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows,parse_dates=[['CRASH_DATE','CRASH_TIME']])
    data.dropna(subset=['LATITUDE','LONGITUDE'],inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time':'date/time'},inplace=True)
    return data

data=load_data(100000)

st.subheader("Raw Data")
st.write(data)