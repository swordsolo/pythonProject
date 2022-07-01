# *_*coding:utf-8 *_*
# author:jijian

def cmp(str1, str2):
    if int(str1 + str2) > int(str2 + str1):
        return 1
    else:
        return 0


def solve(nums):
    # write code here
    if sum(nums) == 0:
        return 0
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1, n - 1):
            if int(str(nums[j]) + str(nums[j + 1])) < int(str(nums[j + 1]) + str(nums[j])):
            # if cmp(str(nums[j]), str(nums[j + 1])):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


    s = ''
    for i in range(n):
        s += str(nums[i])
    return s

nums = [2, 20, 23, 4, 8]
print(solve(nums))