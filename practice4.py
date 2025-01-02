import pandas as pd
df = pd.read_csv('C:/Users/마상위/Desktop/Data/iris.csv')
df
df.info()
df.loc[3,'Petal_Width']
df.iloc[2,3]