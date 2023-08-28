"""
File     : app_climb\pages\02_Dataview.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

import streamlit as st

col1, col2 = st.columns([0.6, 0.4])

if 'df' not in st.session_state:
    st.write("Please upload the gpx file.")
    
else:
    route_df = st.session_state.df
    with col1:
        # 加入網頁文字內容
        st.write("#### 資料檢視(View)")
        
        headview = st.radio(
            "Show data options",
            ('First 5 rows', 'Last 5 rows', 'All'))        
        
        if headview == 'First 5 rows':
            st.write(route_df.head())
        elif headview == 'Last 5 rows':
            st.write(route_df.tail())
        else:
            st.write(route_df)  
    with col2:
        # 加入網頁文字內容
        st.write('#### 資料摘要(Summary)')
        
        # 開始時間
        st.write("Start time: " + route_df['time'][0].strftime('%Y-%m-%d %H:%M:%S'))
        
        # 完成時間
        st.write("Complete time: " + route_df['time'].iloc[-1].strftime('%Y-%m-%d %H:%M:%S'))

        # 期間        
        st.write("Duration: " + str(route_df['time'].iloc[-1] - route_df['time'][0]))
        
        # 資料摘要
        st.write(route_df.describe())
# end