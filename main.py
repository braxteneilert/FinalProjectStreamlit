import streamlit as st
import pandas as pd

st.title("Excel Update App")

df = pd.read_excel("C:\\Users\\Braxten\\OneDrive\\Documents\\Fundamentals_valuation_spreadsheet.xlsx")

st.dataframe(df)

