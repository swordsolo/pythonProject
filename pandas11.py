# *_*coding:utf-8 *_*
# author:jijian
import pandas as pd



df = pd.DataFrame({
    'index': [1, 2, 3],
    'name': ['zhangsan', 'lisi', 'wangwu'],
    'age': [28, 25, 30]
})

df = df.set_index('index')
print(df)
df.to_excel(r'C:\Users\j3ji\people.xlsx')

print('done!')
pl= pd.read_excel(r'C:\Users\j3ji\people.xlsx',header=0)
pl.sort_values(by='age',ascending=False,inplace=True)
print(pl)