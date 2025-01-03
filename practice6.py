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
                marker='s')