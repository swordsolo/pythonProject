# *_*coding:utf-8 *_*
# author:jijian

def func(dividend, divisor):
    remainder = dividend
    result = 0
    while remainder >= divisor:
        i = 0
        while remainder >= divisor ** i:
            i += 1
        i -= 1
        remainder -= divisor ** i
        result += divisor ** (i - 1)
    return result


print(func(23464657, 3435))
