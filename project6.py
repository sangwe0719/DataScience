import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


df = pd.read_csv('C:/Users/마상위/Desktop/Data/user_behavior_dataset.csv')
df = df.iloc[:,3:10]
df.columns = [ 'App_Usage_Time', 'Screen_On_Time', 'Battery_Drain',
 'No_of_Apps', 'Data_Usage', 'Age', 'Gender']
df

dict = {'Male': 'red', 'Female': 'blue'}
colors = list(dict[key] for key in df.Gender)
colors

marker_dict = {'Male': 'o', 'Female': '^'}
markers = list(marker_dict[key] for key in df.Gender)
markers


df.plot.scatter(x='App_Usage_Time',
                y='No_of_Apps',
                s=50,
                c=colors,
                marker='o')

plt.show()


df = pd.read_csv('C:/Users/마상위/Desktop/Data/students.csv')
df

df['초등학교'] = df['초등학교'].str.replace(',', '').astype(int)
df['중학교'] = df['중학교'].str.replace(',', '').astype(int)
df['고등학교'] = df['고등학교'].str.replace(',', '').astype(int)

plt.figure(figsize=(10, 6))

plt.plot(df['연도'], df['초등학교'], label='초등학교', color='blue', marker='o')
plt.plot(df['연도'], df['중학교'], label='중학교', color='green', marker='^')
plt.plot(df['연도'], df['고등학교'], label='고등학교', color='red', marker='s')

plt.title('연도별 초중고 학생 수', fontsize=16)
plt.xlabel('연도', fontsize=12)
plt.ylabel('학생 수', fontsize=12)
plt.xticks(df['연도'], rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False     

plt.tight_layout()
plt.show()