import pandas as pd
import streamlit as st   # only if using Streamlit dashboard

df_d2c = pd.read_csv("data/d2c_funnel.csv")
df_pharma = pd.read_csv("data/pharma_funnel.csv")

industry = st.sidebar.selectbox("Select Industry", ["D2C", "Pharma"])

if industry == "D2C":
    st.dataframe(df_d2c)
else:
    st.dataframe(df_pharma)
