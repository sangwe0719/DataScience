import folium

import os
os.chdir('D:/ds_study/Ch09/')    # displayMap.py 가 있는 폴더지정
import displayMap as dm
import geokakao as gk
import pandas as pd

df_subway = pd.read_csv('d:/data/subway_line_1_8_20231231.csv')
df_addr = pd.read_csv('d:/data/seoul_subway_address_2023.csv')

time_zone = ['t07_08시간대', 't08_09시간대']
df_subway = df_subway.loc[df_subway.호선명 == 2]  # 2호선 추출
df_subway = df_subway.groupby('역명')[time_zone].sum()  # 역별 승객 수 집계
df_subway['탑승객 수'] = df_subway.sum(axis=1)  # 탑승객 수 합계
df_subway.head()

df_merge = pd.merge(df_subway, df_addr, on='역명', how='inner')

# add lat, lon
gk.add_coordinates_to_dataframe(df_merge, '도로명주소')

# 문자열 좌푯값을 숫자로 변환
df_merge.decimalLatitude = pd.to_numeric(df_merge.decimalLatitude)
df_merge.decimalLongitude = pd.to_numeric(df_merge.decimalLongitude)
df_merge.info()

center = df_merge[['decimalLatitude', 'decimalLongitude']].mean().to_list()

# 지도 객체 생성
map = folium.Map(location=center, zoom_start=12)

# 지도에 마커 추가
for i in range(len(df_merge)):
    folium.Marker(location=[df_merge.loc[i, 'decimalLatitude'],
                            df_merge.loc[i, 'decimalLongitude']],
                            icon=folium.Icon(color='red', icon='star')).add_to(map)
dm.showMap(map)

# 지도 객체 생성
map = folium.Map(location=center, zoom_start=12)

for i in range(len(df_merge)):
    folium.CircleMarker(location=[df_merge.loc[i, 'decimalLatitude'],
    df_merge.loc[i, 'decimalLongitude']],
    radius=((df_merge.loc[i, '탑승객 수']/150000)),  # 원의 반지름
    color='red',  # 원의 색
    stroke=False,  # 윤곽선 없음
    fill=True,  # 원의 내부 색
    fill_opacity='50%'  # 원의 내부 색 투명도
    ).add_to(map)

# 지도에 텍스트(역명) 추가
html_start = html = '<div\
style="\
font-size: 12px;\
color: blue;\
background-color:rgba(255, 255, 255, 0.2);\
width:85px;\
text-align:left;\
margin:0px;\
"><b>'
html_end = '</b></div>'

for i in range(len(df_merge)):
    folium.Marker(location=[df_merge.loc[i, 'decimalLatitude'],
    df_merge.loc[i, 'decimalLongitude']],
    icon=folium.DivIcon(
        icon_anchor=(0, 0),  # 텍스트 위치 설정
        html=html_start+df_merge.loc[i, '역명']+html_end
        )).add_to(map)

# 웹 브라우저에 지도 출력
dm.showMap(map)
