"""
File     : app_climb\pages\05_Elevation_chart.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

import streamlit as st
import pandas as pd
# import numpy as np

# 加入網頁文字內容
st.write("#### 登山海拔剖面圖 (Climbing elevation profile)")

if 'df' not in st.session_state:
    st.write("Please upload the gpx file.")
else:
    route_df = st.session_state.df
    
    df = pd.DataFrame({
        'index': route_df['time'],
        'elevation': route_df['elevation']}).set_index('index')
    st.bar_chart(df)
# end