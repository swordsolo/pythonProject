# *_*coding:utf-8 *_*
# author:jijian

import pandas as pd
import matplotlib.pyplot as plt

pl= pd.read_excel(r'C:\Users\j3ji\people.xlsx')
pl.sort_values(by='age',ascending=False,inplace=True)

plt.bar(pl.name,pl.age,color='orange')

plt.title('Student age',fontsize=20)
plt.xlabel('Name',fontsize=20)
plt.ylabel('Age',fontsize=20,rotation='0')
plt.xticks(pl.name,rotation='0')

plt.tight_layout()
imgname='data.jpg'
plt.savefig(imgname)
plt.show()


