import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/mock_funnel.csv')

st.title("📈 Funnel Analysis & KPIs")

# Sidebar filters
persona_filter = st.sidebar.multiselect("Select Persona", df['Persona'].unique())
industry_filter = st.sidebar.multiselect("Select Industry", df['Industry'].unique())

filtered_df = df[
    (df['Persona'].isin(persona_filter) if persona_filter else True) &
    (df['Industry'].isin(industry_filter) if industry_filter else True)
]

# Calculate conversion rates
filtered_df['Lead_to_Client'] = filtered_df['Client'] / filtered_df['Lead'] * 100

# Conditional formatting example
st.dataframe(filtered_df.style.applymap(
    lambda x: 'background-color: #b6fcd5' if x > 50 else ('background-color: #ffb6b9' if x < 20 else ''), 
    subset=['Lead_to_Client']
))

# Plot funnel chart
fig, ax = plt.subplots()
stages = ['Lead', 'MQL', 'SQL', 'Client']
ax.bar(stages, [filtered_df[stage].sum() for stage in stages], color='skyblue')
st.pyplot(fig)

# CSV download
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name='funnel_filtered.csv',
    mime='text/csv'
)
