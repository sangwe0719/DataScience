import pandas as pd
df = pd.read_csv('C:/Users/마상위/Desktop/Data/GNI2014.csv')
df
df.head()
df.shape[0]
df.shape[1]
df['continent'].unique()
df['country'].unique()
df.loc[df['country']== 'Norway',['population','GNI']]
df.loc[df['continent'] == 'Europe',['country']]
df.loc[(df.population> 50000000),['country']]
europe_population = df.loc[df['continent'] == 'Europe',['population']]
europe_population.mean()
df['GNP'] = df['population'] * df['GNI']
Canada_GNP = df.loc[df['country'] == 'Canada', 'GNP'].values[0]
Canada_GNP
higher_country = df[df.GNP > Canada_GNP]
higher_country.GNP.mean()
df.loc[df['continent'] == 'North America',['population']] * 1.1
df['PNP'] = df['GNP'] / df['population']
df.head()