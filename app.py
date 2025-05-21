import folium
import json
import streamlit as st
from streamlit_folium import st_folium

with open("prefecture.json", mode="r", encoding="utf-8") as f:
    prefectures = json.loads(f.read())

def createMap(place_name):
    map = folium.Map(location=(35.78723722411855, 116.09248508465616), zoom_start=6, min_zoom=4, control_scale=True)
    for prefecture in prefectures:
        folium.Marker(
            location=[prefecture['lat'], prefecture['lon']],
            tooltip=prefecture['name_Song'],
            popup=folium.Popup(
                prefecture['description'],
                max_width=300, offset=(0, -20),
            ),
            icon=folium.Icon(color=prefecture['color']),
        ).add_to(map)
    
        if prefecture['name_Song'] == place_name:
            folium.CircleMarker(
            location=[prefecture['lat'], prefecture['lon']],
            radius=50,
            color="#FF6666",
            weight=3,
            fill=False,
            fill_opacity=0.6,
            opacity=1,
        ).add_to(map)

    return map

places = [prefecture['name_Song'] for prefecture in prefectures]

# ここからStreamlit操作
st.set_page_config(layout="wide")
st.markdown("### 北方水滸伝　地図", unsafe_allow_html=True)

# 地名リスト
selected = st.selectbox("地名を選ぶと赤丸で強調されます", places, index=None, placeholder="文字を入力して検索することもできます")

created_map = createMap(selected)
st.write(selected)

# 地図
st_data = st_folium(created_map, width=2000, height=800)