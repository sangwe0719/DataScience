import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder

# (1) 데이터 준비
df = pd.read_csv('d:/data/chipotle.csv')

df.info()
df.iloc[:, [0, 1, 2, 4]].head()

# (2) 데이터 탐색
len(df['Item'].unique())  # 음식의 종류
temp = df[df.item_price == df.item_price.max()]  # 가장 비싼 음식
temp = temp[['Item', 'item_price']].drop_duplicates()
temp

temp = df[df.item_price == df.item_price.min()]  # 가장 저렴한 음식
temp = temp[['Item', 'item_price']].drop_duplicates()
temp

len(df['Transaction'].unique())  # 트랜잭션 수

# 많이 판매된 음식
sales_quantity = df.groupby('Item').count()
sales_quantity = sales_quantity.sort_values('Transaction', ascending=False)
sales_quantity['Transaction']

# 매출 상위 10개 상품
top_ten = sales_quantity.sort_values('Transaction').tail(10)
top_ten = top_ten['Transaction']

top_ten.plot.barh(xlabel='Transaction',  # x축 레이블
                  ylabel='',  # y축 레이블
                  title='Top 10 Items',  # 그래프 제목
                  figsize=(9, 5))
plt.subplots_adjust(left=0.2)  # 그래프 왼쪽 여백
plt.show()

# (3) 연관 분석
# 전처리
temp = df[['Transaction', 'Item']].drop_duplicates()
temp = temp.groupby('Transaction')['Item'].apply(list)
temp

te = TransactionEncoder()
trans_matrix = te.fit(temp).transform(temp)
trans_matrix

basket = pd.DataFrame(trans_matrix, columns=te.columns_)
basket.head()

# 연관규칙 탐색
freq_item = apriori(df=basket, min_support=0.01, use_colnames=True)
freq_item

rules = association_rules(df=freq_item, metric='lift', min_threshold=1,
                          num_itemsets=len(basket))
rules.sort_values('confidence', ascending=False, inplace=True)
rules.head(10)
rules.iloc[0, :].transpose()