import streamlit as st
import pandas as pd

st.title("📊 Growth Dashboard")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Users": [100, 250, 400, 600],
    "Revenue": [1000, 2000, 3500, 5000]
})

st.line_chart(data.set_index("Month")["Users"])
st.bar_chart(data.set_index("Month")["Revenue"])
