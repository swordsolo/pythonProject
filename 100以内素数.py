# *_*coding:utf-8 *_*
# author:jijian

def isPrime(num):
    j=2
    while j*j<=num:
        if num%j==0:
            return False
        j+=1
    return True

def Prime(n):
    list=[]
    for i in range(2,n+1):
        if isPrime(i):
            list.append(i)
    return list



print(Prime(100))