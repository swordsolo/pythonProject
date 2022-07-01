# *_*coding:utf-8 *_*
# author:jijian

def isPrime(num):
    j=2
    while j*j<=num:
        if num%j==0:
            return False
        j+=1
    return True

def cal_Primefactor(num):
    list=[]
    while not isPrime(num):
        i=2
        while i<num:
            if num%i==0:
                num/=i
                list.append(i)
                break
            i+=1
    list.append(int(num))
    return list

print(cal_Primefactor(46))


def factor(num):
    for i in range(2,num):
        if num%i==0:
            print(i,end="*")
            num=int(num/i)
            factor(num)
            return
    print(int(num))

factor(18)

