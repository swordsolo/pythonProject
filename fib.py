# *_*coding:utf-8 *_*
# author:jijiana
# is beautiful
arr = [1, 2, 3, 4, 5, 4, 2]
arr.sort()
res = []
n = len(arr)
print
n
for i in range(1, n - 1):
    if (arr[i] != arr[i + 1] and arr[i] != arr[i - 1]):
        res.append(arr[i])
if (arr[0] != arr[1]):
    res = [arr[0]] + res
if (arr[-1] != arr[-2]):
    res = res + [arr[-1]]
print(res)
