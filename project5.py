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