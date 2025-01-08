import pandas as pd
import seaborn as sns
df1 = pd.DataFrame([[169,58, 1.0],
                    [172, 73, 1.2],
                    [184,82,0.7]],
                    columns = ['height', 'weight', ' eye'])
df2 = pd.DataFrame([[176,71,0.8,'M'],
                    [169,62,0.7,'F'],
                    [158,60,1.3,'M']],
                    columns = ['height', 'weight', ' eye','gender'])
df3 = pd.DataFrame([[3,22],
                    [2,21]],
                   columns = ['grade','age'])
df1
df2
df3
df12 = pd.concat([df1,df2])
df12 = df12.reset_index(drop=True)
df12
df13 = pd.concat([df1,df3], axis=1)
df13

df = sns.load_dataset('tips')
df.head()
p1 = df.pivot_table(index = 'sex', 
columns = 'day', 
values = 'total_bill', 
aggfunc = 'mean' 
)
p1.head()
