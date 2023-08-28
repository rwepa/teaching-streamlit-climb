"""
File     : app_climb\main.py
Title    : Streamlit app for climbing
Date     : 2023.08.18
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
"""

# streamlit 執行方式
# 建立 D:\streamlitdata\app_climb\main.py
# 命令提示字元
# d:
# cd streamlitdata\app_climb
# streamlit run main.py

# 安裝模組
# conda install -c conda-forge gpxpy
# conda install -c conda-forge streamlit
# conda install -c conda-forge folium
# conda install -c conda-forge streamlit-folium

import streamlit as st

st.set_page_config(
    page_title="RWEPA | Visualization Climbing Routes with Python and Streamlit",
)

st.write("#### RWEPA | Visualization Climbing Routes with Python and Streamlit!")

st.markdown(
    """
    - 登山路線視覺化分析平台 - 使用 Python + 免費 streamlit 模組
    - 選取 👈 左側功能列，請從 **Uploadfile** 開始執行平台功能
    
    ##### 平台實作程式碼
    - Code [https://github.com/rwepa/teaching-streamlit-climb]
    
    - 安裝模組
    
      1. conda install -c conda-forge gpxpy
    
      2. conda install -c conda-forge streamlit
    
      3. conda install -c conda-forge folium
    
      4. conda install -c conda-forge streamlit-folium
    
    ##### 參考資源
    - Python - streamlit dashboard 教學 [https://youtu.be/FW-dl-flLvk](https://youtu.be/FW-dl-flLvk)
    - Python - streamlit dashboard 連結 [http://rwepa.blogspot.com/2023/01/python-streamlit-dashboard.html](http://rwepa.blogspot.com/2023/01/python-streamlit-dashboard.html)
    - Python - streamlit dashboard 程式碼 [https://github.com/rwepa/teaching-streamlit](https://github.com/rwepa/teaching-streamlit)
    - Streamlit Chart elements [https://docs.streamlit.io/library/api-reference/charts]    
    """
)
# end
