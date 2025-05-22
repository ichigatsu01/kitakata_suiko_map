import folium
import json
import streamlit as st
from streamlit_folium import st_folium

with open("prefecture.json", mode="r", encoding="utf-8") as f:
    prefectures = json.loads(f.read())

def createMap(mlat, mlon, place_name):
    map = folium.Map(location=(mlat, mlon), zoom_start=6, min_zoom=4, control_scale=True)
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

# 何等かの地名が選択されていたら、地名の説明を表示する
if selected:
    for prefecture in prefectures:
        if prefecture['name_Song'] == selected:
            st.write(prefecture['description'])
            # 選択した場所を地図の中心に出来るんじゃないのか？という実験
            selected_lat, selected_lon = prefecture['lat'], prefecture['lon']
else:
    st.write("いずれかの地名を選ぶと、ここに説明が表示されます。アイコンをクリックしても詳細が見れます")
    # 何も選ばれていない場合、梁山泊を地図の中心に据える
    selected_lat, selected_lon = 35.78723722411855, 116.09248508465616

created_map = createMap(selected_lat, selected_lon, selected)

# 地図
st_data = st_folium(created_map, width=2000, height=600)