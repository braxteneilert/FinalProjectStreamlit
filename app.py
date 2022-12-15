# INF601 - Advanced Programming in Python
# Braxten Eilert
# Final Project
import streamlit as st
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import numpy as np




st.title("Online Stock Ticker")


tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
df = tickerData.history(period='1D', start="2015-1-1", end='2022-12-1')


log_close_price = np.log10(df.Close)
log_price = st.sidebar.checkbox("Log Price")
if log_price:
    df["Close"] = np.log10(df["Close"])

st.line_chart(df.Close)


st.line_chart(df.Volume)










