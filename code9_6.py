import folium

import os
os.chdir('D:/ds_study/Ch09/')    # displayMap.py 가 있는 폴더지정
import displayMap as dm
import pandas as pd

df = pd.read_csv('d:/data/wind.csv')
df.head()

df = df.sample(50, random_state=123)

# 지도의 중심점 구하기
center = [df.lat.mean(), df.lon.mean()]

# 지도 가져오기
map = folium.Map(location=center, zoom_start=5)
dm.showMap(map)

# 측정 위치에 마커 표시하기
for i in range(len(df)):
    folium.Marker(location=[df.lat.iloc[i], df.lon.iloc[i]],
                  icon=folium.Icon(color='blue', icon='flag')).add_to(map)
dm.showMap(map)

# 풍속을 원의 크기로 표시하기
map = folium.Map(location=center, zoom_start=5)  # 마커 없는 지도

for i in range(len(df)):
    folium.CircleMarker(location=[df.lat.iloc[i], df.lon.iloc[i]],
                        radius=(df.spd.iloc[i]**0.5)*2,  # 원의 반지름
                        color='red',  # 원의 색
                        stroke=False,  # 윤곽선 없음
                        fill=True,  # 원의 내부 색
                        fill_opacity='50%'  # 원의 내부 색 투명도
                        ).add_to(map)
dm.showMap(map)
