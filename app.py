import streamlit as st
import pandas as pd
from model import run_mba

st.set_page_config(page_title="🛒 Market Basket Analysis", layout="wide")
st.title("🛍 Real-Time Market Basket Analysis (MBA)")

uploaded_file = st.file_uploader("📂 Upload Transaction Dataset (CSV)", type=["csv"])

if uploaded_file:
    st.success("⏳ Running MBA... Please wait")
    rules = run_mba(uploaded_file)

    st.subheader("📌 Top Association Rules")
    st.dataframe(rules)

    st.subheader("📊 Most Frequently Bought Together")
    top_pairs = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10)
    st.table(top_pairs)

else:
    st.info("Please upload a CSV file to start analysis")
