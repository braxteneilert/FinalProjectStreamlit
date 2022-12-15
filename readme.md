# INF601 - Advanced Programming in Python
# Braxten Eilert
# Final Project

# import packages

import streamlit as st
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import numpy as np



# create title for the streamlit app
st.title("Online Stock Ticker")

# ticker module from yfinance
# 'AAPL', period, start, and end are all customizable
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
# convert into dataframe with time period
df = tickerData.history(period='1D', start="2015-1-1", end='2022-12-1')

# create a checkbox option to log the daily closing price
log_close_price = np.log10(df.Close)
log_price = st.sidebar.checkbox("Log Price")
if log_price:
    df["Close"] = np.log10(df["Close"])

# plot the graph in streamlit
st.line_chart(df.Close)
st.line_chart(df.Volume)

# In order to execute streamlit use command in terminal: streamlit run app.py