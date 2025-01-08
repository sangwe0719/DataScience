import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

