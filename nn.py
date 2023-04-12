import yfinance as yf
import streamlit as st
import pandas as pd
st.write(""" 
## Котировки акций "Норильского никеля" в 2022 году.
""")
ticker_sym='GMKN.ME'
tickerdata=yf.Ticker(ticker_sym)
tickerdf=tickerdata.history(period='1d',start='2022-01-01',end='2023-03-31')
st.write(""" Цена при закрытии торгов""")
st.line_chart(tickerdf.Close)
st.write(""" Объем торгов""")
st.line_chart(tickerdf.Volume)