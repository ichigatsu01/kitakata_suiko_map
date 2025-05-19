import folium
import json
import streamlit as st
from streamlit_folium import st_folium

map = folium.Map(location=(35.78723722411855, 116.09248508465616), zoom_start=6, min_zoom=4, control_scale=True)

with open("prefecture.json", mode="r", encoding="utf-8") as f:
    prefectures = json.loads(f.read())

for prefecture in prefectures:
    # lat = prefecture['lat']
    # lon = prefecture['lon']
    folium.Marker(
    location=[prefecture['lat'], prefecture['lon']],
    tooltip=prefecture['name_Song'],
    popup=folium.Popup(
        prefecture['description'],
        max_width=300, offset=(0, -20),
    ),
    icon=folium.Icon(color="red"),
).add_to(map)

st.subheader('北方水滸伝　地図')
st_data = st_folium(map, width=900, height=700)