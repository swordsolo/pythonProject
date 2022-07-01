# *_*coding:utf-8 *_*
# author:jijian
n = 50
list = [_+1 for _ in range(n)]
# m=len(list)//2
# for i in range(m):
#     list.pop(i)
# print(list)
while len(list)!=1:
    m=len(list)
    if m%2==0:
        m=int(m/2)
    else:
        m=m//2+1
    for i in range(m):
        list.pop(i)
print(list[0])