# *_*coding:utf-8 *_*
# author:jijian

def shellSort(nums):
    n = len(nums)
    step = 2
    group = int(n / step)
    while group > 0:
        for i in range(group):
            j = i + group
            while j < n:
                k = j - group
                key = nums[j]
                while k >=0:
                    if nums[k] > key:
                        nums[k+group] = nums[k]
                        nums[k] = key
                    k -= group
                j += group
        group=int(group/step)
    return nums

if __name__=="__main__":
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(shellSort(nums))

