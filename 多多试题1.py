# *_*coding:utf-8 *_*
# author:jijian
def countvalue(n,x,y):
    list_x=list(x)
    list_y=list(y)
    sum=0
    for i in list(y):
        if i in list_x:
            list_x.remove(i)
            list_y.remove(i)
            n-=1
    for i in range(n):
        sum+=abs(ord(list_x[i])-ord(list_y[i]))
    return sum

print(countvalue(3,"abc","abd"))