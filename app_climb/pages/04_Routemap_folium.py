"""
File     : app_climb\pages\04_Routemap_folium.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

import folium
import streamlit as st
from streamlit_folium import st_folium

# 加入網頁文字內容
st.write("#### 登山地形圖(Routemap)-folium")

tiles_choice = st.radio(
    label="Map tiles options",
    options=('OpenStreetMap', 'CartoDBPositron', 'CartoDBDark_Matter'))

if 'df' not in st.session_state:
    st.write("Please upload the gpx file.")
else:
    route_df = st.session_state.df
    
    # 建立routemap
    lat_mean = route_df["latitude"].mean()
    lng_mean = route_df["longitude"].mean()
    
    route_map = folium.Map(
        location=[lat_mean, lng_mean],
        zoom_start=14,
        tiles=tiles_choice
    )

    # https://fontawesome.com/icons
    tooltip101building = "台北101大樓"
    
    taipei101building_lat = 25.03369
    taipei101building_long = 121.564128
    
    folium.Marker([taipei101building_lat, taipei101building_long],
                  popup="<i>Taipei 101 Building</i>", 
                  tooltip=tooltip101building,
                  icon=folium.Icon(color="red", icon="info-sign")
                  ).add_to(route_map)
                 
    coordinates = [tuple(x) for x in route_df[['latitude', 'longitude']].to_numpy()]
    folium.PolyLine(coordinates, weight=6).add_to(route_map)
    
    tooltip_begin = "開始"
    folium.Marker([route_df['latitude'][0], route_df['longitude'][0]],
                  popup="<i>Start</i>", 
                  tooltip=tooltip_begin,
                  icon=folium.Icon(icon="person-hiking")
                  ).add_to(route_map)
    
    tooltip_end = "結束"
    folium.Marker([route_df['latitude'].iloc[-1], route_df['longitude'].iloc[-1]],
                  popup="<i>Complete</i>",
                  tooltip=tooltip_end,
                  icon=folium.Icon(icon="mountain-sun")
                  ).add_to(route_map)

    # render Folium map in Streamlit
    st_data = st_folium(route_map, height=500, width=800)
# end
