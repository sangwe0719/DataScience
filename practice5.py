import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

favorite = pd.Series( ['WINTER', 'SUMMER', 'SPRING', 'SUMMER', 'SUMMER',
'FALL', 'FALL', 'SUMMER', 'SPRING', 'SPRING'])
favorite
favorite.value_counts()
favorite.value_counts()/favorite.size
fd = favorite.value_counts()
type(fd)
fd["SUMMER"]
fd.iloc[2]

fd.plot.bar(xlabel = 'Season',
            ylabel = 'Frequency',
            rot = 0,
            title = 'Favorite Season')
plt.show()

fd.plot.barh(xlabel = 'Season',
            ylabel = 'Frequency',
            rot = 0,
            title = 'Favorite Season')
plt.subplots_adjust(left = 0.2)
plt.show()

fd.plot.pie(ylabel = '',
            autopct = '%1.f%%',
            title = 'Favorite Season')
plt.show()

colors = pd.Series([2,3,2,1,1,2,2,1,3,2,1,3,2,1,2])
fd = colors.value_counts()
fd
fd.index
fd.index = ['red', 'green', 'blue']
fd

fd.plot.bar(xlabel='Color', ylabel='Frequency', rot=0, title='Favorite Color')
plt.show()

fd.plot.pie(ylabel='', autopct='%1.0f%%', title='Favorite Color')
plt.show()

mydata = [60, 62, 64, 65, 68, 69, 120]
mydata = pd.Series(mydata)
mydata.quantile(0.25) # Q1
mydata.quantile(0.5) # Q2
mydata.quantile(0.75) # Q3
mydata.quantile([0.25, 0.5, 0.75])
mydata.quantile(np.arange(0, 1, 0.1))
mydata.describe()

df = pd.read_csv('C:/Users/마상위/Desktop/Data/cars.csv')
dist = df['dist']
dist
dist.plot.hist()
plt.show()

dist.value_counts(bins = 6, sort = False)

dist.plot.hist(bins=6, 
title='Braking distance', 
xlabel='distance', 
ylabel='frequency', 
color='g')
               
plt.show()