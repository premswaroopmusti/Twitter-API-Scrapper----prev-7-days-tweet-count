import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import preprocessing
import tweepy

df = pd.read_excel("fo_mktlots.xlsx")

saath_din = preprocessing.pichle_saath_din(df)


st.sidebar.title("Twitter-Sentiment-Analysis")
time = 'Last 7 days count'


if(time == 'Last 7 days count'):
    st.header("Previous 7 days count")
    st.bar_chart(data = saath_din, x = 'keyword',y = 'count')

