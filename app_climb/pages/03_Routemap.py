"""
File     : app_climb\pages\03_Routemap.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

import streamlit as st
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt

# 加入網頁文字內容
st.write("#### 登山路線圖(Routemap)")

if 'df' not in st.session_state:
    st.write("Please upload the gpx file.")
else:
    route_df = st.session_state.df 
    
    # 建立散佈圖
    fig = plt.figure()
    plt.scatter(route_df['longitude'], route_df['latitude'])
    
    # 加入101圖示
    taipei101building_lat = 25.03369
    taipei101building_long = 121.564128
    plt.plot(taipei101building_long, taipei101building_lat, marker="^", markersize=10, markeredgecolor="red", markerfacecolor="green")
    plt.text(taipei101building_long, taipei101building_lat,'  Taipei 101 Building')
    
    # 加入開始圖示
    start_lat = route_df['latitude'][0]
    start_long = route_df['longitude'][0]
    plt.plot(start_long, start_lat, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="green")
    plt.text(start_long, start_lat,'  Start')
    
    # 加入完成圖示
    complete_lat = route_df['latitude'].iloc[-1]
    complete_long = route_df['longitude'].iloc[-1]
    plt.plot(complete_long, complete_lat, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="green")
    plt.text(complete_long, complete_lat,'  Complete')
    
    # 新增標題
    plt.title('Mountaineering Route Map' + '-' + route_df['time'][0].strftime('%Y-%m-%d'))
    
    # 新增x軸標題
    plt.xlabel("Longitude")
    
    # 新增y軸標題
    plt.ylabel("Latitude")
    
    # 新增網格線
    plt.grid()    
    
    # 取消科學符號表示
    plt.ticklabel_format(useOffset=False)
    
    # X軸刻度文字旋轉45度
    plt.xticks(rotation = 45) 
    
    # 繪圖
    st.pyplot(fig)
# end