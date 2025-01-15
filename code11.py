import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/마상위/Desktop/Data/paired_ttest.csv')
df.head()
df[['before','after']].mean()
(df['after']-df['before']).mean()

fig, axes = plt.subplots(nrows=1, ncols=2)
df['before'].plot.box(grid=False, ax=axes[0])
plt.ylim([60,100])
df['after'].plot.box(grid=False, ax=axes[1])
plt.show()

stats.shapiro(df['after']-df['before'])

result = stats.ttest_rel(df['before'],df['after'])
result

men = [10,10]
women = [15,65]
stats.chi2_contingency([men,women])

Group_A = [7,3]
Group_B = [2,9]

stats.chi2_contingency([Group_A,Group_B])[3]
stats.fisher_exact([Group_A,Group_B])