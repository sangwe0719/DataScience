import folium
import geokakao as gk

import os
os.chdir('C:/Users/마상위/Desktop/DataScience/')    # displayMap.py 가 있는 폴더지정
import displayMap as dm

loc = gk.convert_address_to_coordinates('강원특별자치도 강릉시 창해로 514')
loc
map = folium.Map(location=loc, zoom_start=13)  # 지도 객체 생성
folium.Marker(location=loc,  # 마커 표시
              icon=folium.Icon(color='red', icon='star')).add_to(map)
dm.showMap(map)  # 웹 브라우저에 지도 표시
