import streamlit as st
import pandas as pd

st.set_page_config(page_title="UIDAI Dashboard", layout="wide")

st.title("UIDAI Hackathon Dashboard")
st.success("If you see this, Streamlit is working perfectly ✅")

data = {
    "Service": ["Authentication", "Authentication", "Update", "Update"],
    "Status": ["Success", "Fail", "Success", "Fail"],
    "Count": [1500, 180, 1200, 130]
}

df = pd.DataFrame(data)

st.subheader("Sample Aadhaar-style Data")
st.dataframe(df)

st.subheader("Service-wise Count")
st.bar_chart(df.set_index("Service")["Count"])
