import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 DT Fellowship Simulation - Growth Dashboard")

# Sample Data
data = {
    "Stage": ["Awareness", "Interest", "Consideration", "Purchase", "Retention"],
    "Users": [1000, 650, 400, 200, 120]
}
df = pd.DataFrame(data)

# Show data in a table
st.subheader("Data Table")
st.dataframe(df)

# Line Chart
st.subheader("Line Chart")
st.line_chart(df.set_index("Stage"))

# Bar Chart (Matplotlib)
st.subheader("Bar Chart (Matplotlib)")
fig, ax = plt.subplots()
ax.bar(df["Stage"], df["Users"], color="skyblue")
ax.set_xlabel("Stage")
ax.set_ylabel("Users")
ax.set_title("Users per Stage")
st.pyplot(fig)
