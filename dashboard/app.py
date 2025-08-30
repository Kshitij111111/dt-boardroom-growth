import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📊 Growth Engineering Dashboard – DT Fellowship Simulation")

# Load data
try:
    df = pd.read_csv("data/mock_funnel.csv")
    st.success("Data loaded successfully!")
except FileNotFoundError:
    st.error("mock_funnel.csv not found in /data folder.")
    st.stop()

# Show raw data
st.subheader("Raw Funnel Data")
st.dataframe(df)

# Simple funnel visualization
if "stage" in df.columns and "users" in df.columns:
    st.subheader("Funnel Visualization")
    fig = px.funnel(df, x="users", y="stage", title="User Funnel")
    st.plotly_chart(fig)
else:
    st.warning("CSV must contain columns: stage, users")

# Footer
st.markdown("---")
st.caption("Built for DT Boardroom Lab — Growth Engineering")
