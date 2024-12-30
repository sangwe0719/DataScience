import pandas as pd
import numpy as np
sales = pd.Series([781,650,705,406,580,450,550,640])
sales.index = ['A','B','C','D','E','F','G','H']
sales
print(len(sales))
sales.iloc[2]
sales.loc['F']
sales.iloc[3:6]
sales.loc[['A','B','D']]
sales.loc[(sales < 500)|(sales > 700)]
B = sales.loc['B']
sales.loc[sales > B]
sales.loc[sales < 600].index
sales.loc[sales < 600] * 1.2
sales.mean()
sales.sum()
sales.std()
sales.loc[['A','C']]=[810,820]
sales
sales.loc['J'] = 400
sales
sales.drop('J')
sales
sales = sales.drop('J')
sales