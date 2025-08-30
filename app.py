import streamlit as st
import pandas as pd

st.title("🚀 DT Fellowship Growth Simulation - Interactive Dashboard")

# --- Inputs from User ---
st.sidebar.header("📌 Simulation Controls")
initial_users = st.sidebar.number_input("Initial Users", min_value=10, max_value=1000, value=100, step=10)
growth_rate = st.sidebar.slider("Monthly Growth Rate (%)", 1, 100, 20)
months = st.sidebar.slider("Number of Months", 3, 24, 12)

# --- Simulation Logic ---
data = {"Month": [], "Users": [], "Revenue": []}
users = initial_users
for m in range(1, months+1):
    users = users * (1 + growth_rate/100)
    revenue = users * 2.5   # assume avg ₹2.5 revenue per user
    data["Month"].append(f"Month {m}")
    data["Users"].append(int(users))
    data["Revenue"].append(int(revenue))

df = pd.DataFrame(data)

# --- Display ---
st.subheader("📋 Simulated Data")
st.dataframe(df)

st.subheader("📈 Line Chart - Users Growth")
st.line_chart(df.set_index("Month")["Users"])

st.subheader("📊 Bar Chart - Revenue Growth")
st.bar_chart(df.set_index("Month")["Revenue"])
