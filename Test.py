import pandas as pd
import matplotlib.pyplot as plt
import folium
import geokakao as gk
import os
from folium import plugins
import random
import displayMap as dm

df1 = pd.read_csv('C:/Users/마상위/Desktop/Data/seoul_201512.csv')
df2 = pd.read_csv('C:/Users/마상위/Desktop/Data/seoul_201606.csv')
df3 = pd.read_csv('C:/Users/마상위/Desktop/Data/seoul_201612.csv')
df4 = pd.read_csv('C:/Users/마상위/Desktop/Data/seoul_201706.csv')
df5 = pd.read_csv('C:/Users/마상위/Desktop/Data/seoul_201712.csv')

df = pd.concat([df1,df2,df3,df4,df5])
df = df.reset_index(drop=True)

df5

top10 = (
    df5.groupby('행정동명')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index(name='점포수')
)

top10

file_paths = [
    "/mnt/data/seoul_201512.csv",
    "/mnt/data/seoul_201606.csv",
    "/mnt/data/seoul_201612.csv",
    "/mnt/data/seoul_201706.csv",
    "/mnt/data/seoul_201712.csv",
]

# 파일 이름에서 수집 연월 추출
file_dates = ["2015-12", "2016-06", "2016-12", "2017-06", "2017-12"]

# 모든 데이터를 하나의 데이터프레임으로 병합, 수집연월 열 추가
all_data = []
for file_path, date in zip(file_paths, file_dates):
    df = pd.read_csv(file_path, encoding="utf-8")
    df["수집연월"] = date
    all_data.append(df)

# 병합
merged_data = pd.concat(all_data, ignore_index=True)

# 상권업종대분류명 기준으로 점포 수 집계
trend_data = merged_data.groupby(["수집연월", "상권업종대분류명"]).size().reset_index(name="점포수")

# 피벗 테이블로 데이터 변환
pivot_data = trend_data.pivot(index="수집연월", columns="상권업종대분류명", values="점포수").fillna(0)

# 선 그래프 그리기
pivot_data.plot(kind="line", figsize=(12, 6), marker='o', title="수집연월에 따른 점포수 변화 (상권업종대분류명 기준)")
plt.xlabel("수집연월")
plt.ylabel("점포 수")
plt.legend(title="상권업종대분류명", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

import pandas as pd
import folium
from folium import plugins
import random

# 데이터 로드
data_201712 = pd.read_csv("C:/Users/마상위/Desktop/Data/seoul_201712.csv", encoding="utf-8")

# 역삼1동 데이터 필터링
ys = df5[df5['행정동명'] == '역삼1동']

# 색상 매핑을 위한 딕셔너리 생성 (상권업종대분류명별 색상)
ct = ys['상권업종대분류명'].unique()
colors = ['red','orange', 'yellow', 'green' ,'blue', 'purple', 'brown', 'pink', 'gray']
color_map = {category: colors[i % len(colors)] for i, category in enumerate(ct)}

m = folium.Map(location=map_center, zoom_start=15)
for _, row in data_yeoksam1.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color=color_map[row['상권업종대분류명']],
        fill=True,
        fill_color=color_map[row['상권업종대분류명']],
        fill_opacity=0.6,
        popup=f"{row['상호명']} ({row['상권업종대분류명']})"
    ).add_to(m)
    
dm.showMap(m)


color_map = {category: f"#{''.join([random.choice('0123456789ABCDEF') for _ in range(6)])}" for category in ct}

# 지도 생성 (중심점: 역삼1동의 평균 위도와 경도)
map_center = [ys['위도'].mean(), ys['경도'].mean()]
m = folium.Map(location=map_center, zoom_start=15)

# 점 추가
for _, row in ys.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color=color_map[row['상권업종대분류명']],
        fill=True,
        fill_color=color_map[row['상권업종대분류명']],
        fill_opacity=0.6,
        popup=f"{row['상호명']} ({row['상권업종대분류명']})"
    ).add_to(m)

# 범례 추가
legend_html = '<div style="position: fixed; bottom: 50px; left: 50px; width: 250px; height: auto; background-color: white; z-index:9999; padding: 10px; border: 2px solid grey;"><h4>상권업종대분류명 색상</h4>'
for category, color in color_map.items():
    legend_html += f'<p style="margin: 0;"><span style="display: inline-block; width: 15px; height: 15px; background-color: {color}; margin-right: 10px;"></span>{category}</p>'
legend_html += '</div>'
m.get_root().html.add_child(folium.Element(legend_html))

# 지도 표시
m.save("yeoksam1_map.html")
dm.showMap(m)

df5['상권업종대분류명'].value_counts()

district_store_counts = data_201712.groupby('시군구명').size().reset_index(name='점포수')

# 서울의 구 중심 좌표 (예시 좌표, 실제 데이터에 따라 수정 가능)
district_coords = {
    '강남구': [37.517236, 127.047325],
    '강동구': [37.530125, 127.12377],
    '강북구': [37.639774, 127.025599],
    '강서구': [37.550964, 126.849532],
    '관악구': [37.478406, 126.951613],
    '광진구': [37.538712, 127.082366],
    '구로구': [37.495485, 126.887820],
    '금천구': [37.456979, 126.895569],
    '노원구': [37.654301, 127.056793],
    '도봉구': [37.668763, 127.046574],
    '동대문구': [37.574354, 127.039896],
    '동작구': [37.512409, 126.939632],
    '마포구': [37.566324, 126.901491],
    '서대문구': [37.579172, 126.936681],
    '서초구': [37.483595, 127.032681],
    '성동구': [37.563506, 127.036215],
    '성북구': [37.589646, 127.016385],
    '송파구': [37.514575, 127.112622],
    '양천구': [37.516769, 126.866521],
    '영등포구': [37.526371, 126.896337],
    '용산구': [37.532475, 126.990745],
    '은평구': [37.602984, 126.929319],
    '종로구': [37.572602, 126.979999],
    '중구': [37.563756, 126.997602],
    '중랑구': [37.606991, 127.092759]
}

# 지도 생성 (서울 중심 좌표)
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 구별 점포 수를 지도에 추가
for _, row in district_store_counts.iterrows():
    district = row['시군구명']
    count = row['점포수']
    if district in district_coords:  # 좌표가 있는 경우만 처리
        folium.CircleMarker(
            location=district_coords[district],
            radius=count / 1000,  # 점포 수에 따라 반경 조정 (예: 1000개당 1 반경)
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"{district}: {count} 점포"
        ).add_to(seoul_map)

# 지도 저장
seoul_map.save("seoul_district_store_counts.html")
dm.showMap(seoul_map)