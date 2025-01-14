import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import konlpy

# (1) 데이터 준비
df = pd.read_csv('d:/data/movie1_review.csv')
df

# (2) 형태소 분석기 정의
kkma = konlpy.tag.Kkma() # 형태소 분석기 꼬꼬마(Kkma)

# (3) 단어 데이터프레임 만들기
nouns = df['Review'].apply(kkma.nouns)
nouns

nouns = nouns.explode()
nouns

# (4) 전처리 실시
# 모시 -> 티모시, imax -> 아이맥스,...
nouns[nouns=='모시'] = '티모시'
nouns[nouns=='IMAX'] = '아이맥스'
nouns[nouns=='파트3'] = '3편'

# 글자 수 2개 이상인 단어만 추출
df_word = pd.DataFrame({'word' : nouns})
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count >= 2')
df_word

# 단어 빈도수 집계 및 정렬
df_word = df_word.groupby('word', as_index = False)
df_word = df_word.count().sort_values('count', ascending = False)
df_word

# 불필요한 단어 제거
del_idx = df_word.loc[df_word.word.isin(['영화', '편이', '영화관', '파트' ])].index
df_word = df_word.drop(index=del_idx)

# (5) 워드클라우드 작성
# 빈도수 상위 10개 단어
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

df_top10 = df_word.iloc[:10,:].sort_values('count', ascending=True)
df_top10.plot.barh(x='word', y='count')
plt.show()

# 워드클라우드
dic_word = df_word.set_index('word').to_dict()['count']
dic_word

wc = WordCloud(random_state=123,
               font_path='c:/Windows/Fonts/malgun.ttf',
               width=400,
               height=400,
               background_color='white')

img_wordcloud = wc.generate_from_frequencies(dic_word) # 워드클라우드 → 이미지로

plt.figure(figsize = (10, 10)) # 크기 지정하기
plt.axis('off') # 축 없애기
plt.imshow(img_wordcloud) # 결과 보여주기
plt.show() # 결과를 화면에 출력

# (6) 클라우드의 모양과 글씨 색상 변경
import PIL
import numpy as np

icon = PIL.Image.open('d:/data/cloud.png').convert("RGBA")
img = PIL.Image.new(mode = 'RGBA', size=icon.size, color=(255, 255, 255))
img.paste(icon, icon)
img = np.array(img)

wc = WordCloud(random_state=123,
               font_path='c:/Windows/Fonts/malgun.ttf',
               width=400,
               height=400,
               background_color='white',
               mask=img,
               colormap='inferno')

img_wordcloud = wc.generate_from_frequencies(dic_word) # 워드클라우드 → 이미지

plt.figure(figsize = (10, 10)) # 크기 지정하기
plt.axis('off') # 축 없애기
plt.imshow(img_wordcloud) # 결과 보여주기
plt.show() # 결과를 화면에 출력