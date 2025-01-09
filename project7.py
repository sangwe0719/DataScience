import pandas as pd
from scipy import stats
df = pd.read_csv('C:/Users/마상위/Desktop/Data/airquality.csv')
df

df.isnull().sum()
df2 = df.dropna()
df2.head()
df3 = df.fillna(df.mean(numeric_only=True))
df3.head()
wind_zscore = zscore(airquality_df['Wind'])
outliers = airquality_df[abs(wind_zscore) > 2]
outliers
