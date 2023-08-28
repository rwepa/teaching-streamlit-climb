"""
File     : app_climb\pages\01_Uploadfile.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

# 載入模組
import streamlit as st
import gpxpy
import pandas as pd

# 加入網頁文字內容
st.write("#### 上傳GPX檔案 (Upload GPX File)")

st.write("Downlaod gpx file:　[https://github.com/rwepa/teaching-streamlit-climb/blob/main/app_climb/data/climb-2023-08-16-101building.gpx]")
# 上傳檔案
uploaded_file = st.file_uploader(label="Upload a gpx file", type=["gpx"], accept_multiple_files=False)

if uploaded_file is not None:

    # gpx = gpxpy.parse(open("data/climb-2023-08-16-101building", encoding="utf-8"))
    gpx = gpxpy.parse(uploaded_file)
           
    # 解析 GPX 資料
    route_info = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                route_info.append({
                    'latitude': point.latitude,
                    'longitude': point.longitude,
                    'elevation': point.elevation,
                    'time': point.time
                })
                
    # 檢視前5筆資料
    # route_info[:5]

    # 轉換為 data.frame
    # latitude(緯度) longitude(經度) elevation(高度)
    route_df = pd.DataFrame(route_info) #453*4
    
    # 刪除 timezone
    route_df['time'] = route_df['time'].apply(lambda x: x.replace(tzinfo=None))
    
    # 將資料框儲存為工作階段狀態 (session_state)
    st.session_state.df = route_df
        
    st.write("GPX上傳成功!")
# end