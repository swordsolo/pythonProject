# *_*coding:utf-8 *_*
# author:jijian

n=100000
m=0
l=[_+1 for _ in range(n)]
print(l)
list=[]
for i in range(1,n+1):
    m+=i
    list.append(m)
print(list)
for i in range(n):
    for j in range(i):
        if list[i]-list[j]==n:
            print(l[j+1],l[i])