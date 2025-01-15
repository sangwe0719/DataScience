import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/마상위/Desktop/Data/iris.csv')
setosa = df.loc[df.Species=='setosa','Petal_Length']
stats.shapiro(setosa)
virginica = df.loc[df.Species=='virginica','Petal_Length']
stats.shapiro(virginica)
stats.levene(setosa, virginica)
result = stats.ttest_ind(setosa, virginica, equal_var=True)
result

