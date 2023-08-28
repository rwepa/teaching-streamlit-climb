"""
File     : app_climb\pages\06_RoutemapExcel.py
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
import io
from datetime import datetime

# 加入網頁文字內容
st.write("#### 儲存Excel檔案 (Export to Excel)")

buffer = io.BytesIO()

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d_%H%M%S")

if 'df' not in st.session_state:
    st.write("Please upload the gpx file.")
else:
    route_df = st.session_state.df
    
    filename = 'climb_' + dt_string + ".xlsx"
    
    sheetname = 'climb_' + dt_string
    
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        
        # Write each dataframe to a different worksheet.
        route_df.to_excel(writer, sheet_name=sheetname, index=False)                
        writer.save()        
        st.download_button(
            label="Download Excel File",
            data=buffer,
            file_name=filename,
            mime="application/vnd.ms-excel"
        )
        # 關閉 Pandas Excel writer
        writer.close()
# end