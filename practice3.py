import pandas as pd
import numpy as np
temp = pd.Series([-0.8, -0.1, 7.7, 13.8, 18.0, 22.4,
25.9, 25.3, 21.0, 14.0, 9.6, -1.4])
temp
temp.index
print(len(temp))
print(len(['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']))
temp.index = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
temp.iloc[2]
march = temp.loc['3월']
temp.loc[temp < march]
temp.where(temp >= 15)
temp.where(temp >= 15).dropna()
temp + 1
2 * temp + 0.1
temp + temp
temp.loc[temp >= 15] + 1
temp.sum()
temp.mean()
temp.median()
temp.describe()