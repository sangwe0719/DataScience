import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import konlpy

df = pd.read_fwf('d:/data/반기문_국회_연설문.txt').iloc[:, 0]
df.head()

kkma = konlpy.tag.Kkma()

nouns = df.apply(kkma.nouns)
nouns = nouns.explode()
nouns

# 글자 수 2개 이상인 단어만 추출
df_word = pd.DataFrame({'word': nouns})
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count >= 2')
df_word

# 단어 빈도수 집계 및 정렬
df_word = df_word.groupby('word', as_index=False)
df_word = df_word.count().sort_values('count', ascending=False)
df_word.head(10)

dic_word = df_word.set_index('word').to_dict()['count']
dic_word

wc = WordCloud(random_state=123,
               font_path='c:/Windows/Fonts/malgun.ttf',
               width=400,
               height=400,
               background_color='white')
img_wordcloud = wc.generate_from_frequencies(dic_word)  # 워드클라우드 -> 이미지

plt.figure(figsize=(10, 10))  # 크기 지정하기
plt.axis('off')  # 축 없애기
plt.imshow(img_wordcloud)  # 결과 보여주기
plt.show()  # 결과를 화면에 출력