import streamlit as st
import pandas as pd

st.title("Municipal Budget Intelligence")

@st.cache_data
def load_data(path="data.csv"):
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_data()
    st.header("Budget data")
    st.dataframe(df)
    st.markdown("---")
    total_budget = df["budget"].sum()
    total_spending = df["actual"].sum()
    st.metric("Total Budget", f"${total_budget:,.0f}")
    st.metric("Actual Spending", f"${total_spending:,.0f}")
    alerts = df[df["actual"] > df["budget"]]
    if not alerts.empty:
        st.warning(f"{len(alerts)} departments exceeded budget")
    else:
        st.success("No departments exceeded budget")
