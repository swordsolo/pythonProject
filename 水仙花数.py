# *_*coding:utf-8 *_*
# author:jijian
def isDaffodil(num):
    list = []
    tmp=num
    while num != 0:
        mod = num % 10
        num //= 10
        list.append(mod)
    n = len(list)
    sum = 0
    for i in list:
        sum += i ** n
    if sum==tmp:
        return True
    return False

def sum_Daffodil(n):
    list = []
    for i in range(n):
        if isDaffodil(i) and i>10:
            list.append(i)
    return list


print(sum_Daffodil(1000000))
