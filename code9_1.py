import folium
import geokakao as gk

import os
os.chdir('C:/Users/마상위/Desktop/DataScience/')    # displayMap.py 가 있는 폴더지정
import displayMap as dm

# 지도 중심의 좌표를 알 때
loc = [37.54, 127.05]  # 위도, 경도
map = folium.Map(location=loc)  # 지도 객체 생성
dm.showMap(map)  # 웹 브라우저에 지도 표시

# 지도 중심의 주소를 알 때
loc = gk.convert_address_to_coordinates('경기 용인시 수지구 죽전로 152')
loc  # 지도의 중심 좌표
#map = folium.Map(center=loc, zoom_start=16)  # 지도 객체 생성
map = folium.Map(location=loc, zoom_start=16)  # 지도 객체 생성
dm.showMap(map)  # 웹 브라우저에 지도 표시