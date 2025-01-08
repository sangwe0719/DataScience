import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/마상위/Desktop/Data/mtcars.csv')
df

df.plot.scatter(x='wt', y = 'mpg')
plt.show()

df.plot.scatter(x='wt',
                y='mpg',
                s=50,
                c='red',
                marker='*')
plt.show()

vars = ['mpg', 'disp', 'drat', 'wt']
pd.plotting.scatter_matrix(df[vars])
plt.show()

df = pd.read_csv('C:/Users/마상위/Desktop/Data/iris.csv')
dict = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = list(dict[key] for key in df.Species)
colors

df.plot.scatter(x='Petal_Length', 
y='Petal_Width', #
s=30, 
c=colors, 
marker='o') 
plt.show()

beers = [5,2,9,8,3,7,3,5,3,5]
bal = [0.1,0.03,0.19,0.12,0.04,0.0095,0.07,
       0.06,0.02,0.05]

dict = {'beers': beers, 'bal': bal}
df= pd.DataFrame(dict)
df

df.plot.scatter(x='beers', y='bal',
title='Beers~Blood Alcohol Level')