import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('data/mock_funnel.csv')

# Strip extra spaces from column names
df.columns = df.columns.str.strip()

# Make sure the required columns exist
required_cols = ['Persona', 'Industry', 'Stage', 'Response Rate', 'Drop off Reason', 'Campaign Message Summary']
for col in required_cols:
    if col not in df.columns:
        st.error(f"Column '{col}' is missing in your CSV file!")
        st.stop()

st.title("📊 Growth Dashboard")

# --- Sidebar filters ---
persona_filter = st.sidebar.multiselect("Select Persona", df['Persona'].unique())
industry_filter = st.sidebar.multiselect("Select Industry", df['Industry'].unique())

# --- Apply filters safely ---
filtered_df = df.copy()

if persona_filter:
    filtered_df = filtered_df[filtered_df['Persona'].isin(persona_filter)]

if industry_filter:
    filtered_df = filtered_df[filtered_df['Industry'].isin(industry_filter)]

# Display filtered data
st.dataframe(filtered_df)
