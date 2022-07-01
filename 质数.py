# *_*coding:utf-8 *_*
# author:jijian
def isprime(n):
    i=2
    while i*i<n:
        if n%i==0:
            return 0
        i+=1
    return 1

def listprime(n):
    list=[]
    for i in range(2,n):
        if isprime(i):
            list.append(i)
    return list

print(listprime(100))