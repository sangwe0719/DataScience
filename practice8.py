import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.image as mpimg
import plotly.graph_objects as go
import webbrowser
import plotly.express as px


df = sns.load_dataset('flights')
df.head()
sns.set_theme(style="whitegrid", rc={"figure.figsize": (8, 5)})
sns.set_palette('hls', 12)
sns.lineplot(data=df, 
x='year', 
y='passengers', 
hue='month'
)
plt.show()

df = pd.read_csv('C:/Users/마상위/Desktop/Data/crimeRatesByState2005.csv')
df.head()
sns.set_theme(rc={'figure.figsize':(7,7)})

sns.scatterplot(
data=df,
x="murder", 
y="burglary", 
size="population", 
sizes=(20, 4000), 
hue="state", 
alpha=0.5, 
legend=False
)

plt.xlim(0, 12)

for i in range(0, df.shape[0]):
    plt.text(x=df.murder[i], y =df.burglary[i], s=df.state[i],
             horizontalalignment = 'center', size = 'small', color = 'dimgray')

plt.show()

len(df.state.value_counts())

plt.rcParams['font.family'] ='Malgun Gothic' # 한글 처리
plt.rcParams['axes.unicode_minus'] = False # 한글 처리
# 데이터 준비
df = sns.load_dataset('titanic')
df.head()
dict1 = {0:'사망', 1:'생존'}
dict2 = {'male':'남성', 'female':'여성'}
df = df.replace({'survived': dict1})
df = df.replace({'sex': dict2})
df.head()

props = lambda key: {'color': 'lightgreen' if '생존' in key else 'yellow'}
# 그래프 작성
mosaic(data = df.sort_values('sex'),
index = ['sex', 'survived'],
properties = props, # 타일 색상 변경
axes_label = True, # 축 레이블 표시
title='타이타닉 남녀 생존비율' # 그래프 제목
)
plt.show()

def radar(df, fills, min_max, title=''):
    fig = go.Figure()
    categories = df.columns.to_list()
    categories.append(categories[0])
    i=0
    while (i < len(df)) :
        scores = df.iloc[i,:].to_list()
        scores.append(scores[0])
        fig.add_trace(go.Scatterpolar(
            r = scores, # 축의 값
            theta = categories, # 축의 레이블
            fill = fills[i], # 다각형 채우기 색
            name = df.index[i] # 다각형 레이블
        ))
        i += 1
    
        fig.update_layout(
            polar_radialaxis_visible = True,
            polar_radialaxis_range = min_max,
            showlegend = True,
            margin_t = 50, # 상단 여백
            margin_l = 100, # 좌측 여백
            margin_r = 100, # 우측 여백
            margin_b = 25, # 하단 여백
            width = 700, # 그래프의 폭(pixel)
            height = 700, # 그래프의 높이(pixel)
            title_text = title, # 그래프 제목
            title_font_size = 30, # 제목 폰트사이즈
            font_size=20 # 폰트사이즈
    )
# 그래프 저장 & display
    plt.axis('off')
    fig.write_image('rader.png')
    plt.imshow(mpimg.imread('rader.png'))
plt.show()

df = pd.read_csv('C:/Users/마상위/Desktop/Data/GNI2014.csv')
df.head()

fig = px.treemap(data_frame = df,
path=['continent', 'iso3'], # 데이터의 계층구조
values='population', # 타일 면적기준 컬럼
color='GNI', # 색온도 기준 컬럼
color_continuous_scale='Bluyl' # 컬러 팔레트
)

plt.axis('off')

fig.update_layout(margin_t=50, margin_l=25, # 여백 설정
margin_r=25, margin_b=25,
width = 800, # 그래프의 폭(pixel)
height = 600, # 그래프의 높이(pixel)
title_text = 'GNI 2014', # 그래프 제목
title_font_size = 20 # 제목 폰트 크기
)

fig.write_html('C:/Users/마상위/Desktop/Data/treemap.html') # html 파일로 결과 저장
webbrowser.open('C:/Users/마상위/Desktop/Data/treemap.html')