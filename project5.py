import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/마상위/Desktop/Data/user_behavior_dataset.csv')

models = df['Device_Model'] 
usage_time = df['App_Usage_Time'] 
md = models.value_counts()
models.value_counts()/models.size

md.plot.bar(xlabel = 'Models',
            ylabel = 'Frequency',
            rot = 0,
            title = 'Smartphone Models')
plt.show()

usage_time.mean()
usage_time.median()

usage_time
usage_time.plot.hist(bins = 6)
plt.show()

usage_time.plot.box(title = 'Usage Time')
plt.show()
operating_system = df['Operating_System']
operating_system.value_counts()

df.boxplot(column='App_Usage_Time',
           by ='Operating_System',
           grid= False)
plt.suptitle('')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2)
df['App_Usage_Time'].plot.hist(ax=axes[0],bins = 6)
df['App_Usage_Time'].plot.box(ax=axes[1])
plt.show()