import pandas as pd
df = pd.read_csv('C:/Users/마상위/Desktop/Data/user_behavior_dataset.csv')
models = df['Device_Model'] 
usage_time = df['App_Usage_Time'] 
md = models.value_counts()
md