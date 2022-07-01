# *_*coding:utf-8 *_*
# author:jijian
def mergeSort(nums):
    mid = len(nums) // 2
    if mid == 0:
        return nums
    left, right = nums[0:mid], nums[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result

if __name__ == "__main__":
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(mergeSort(nums))