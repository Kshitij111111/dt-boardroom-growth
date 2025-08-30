import streamlit as st

st.title("🤖 AI-Driven Personalized Messaging Preview")

persona = st.selectbox("Select Persona", ["CTO D2C", "COO Pharma", "CMO Construction"])
industry = st.selectbox("Select Industry", ["D2C", "Pharma", "Construction"])

st.write("### Mock AI-Generated Email Preview")

# Example AI output
email_preview = f"""
Hi {persona},

We noticed {industry} companies are achieving rapid growth using AI-driven systems.
Here's how your organization can leverage AIDCA strategies:

- Attention: Innovative growth insights
- Interest: Benchmark your metrics
- Desire: Personalized solutions
- Conviction: Proven success stories
- Action: Schedule a demo today

Regards,
DT Growth Team
"""
st.code(email_preview)
