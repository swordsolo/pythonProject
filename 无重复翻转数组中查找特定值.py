# *_*coding:utf-8 *_*
# author:jijian

def search(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = int((begin + end) / 2)
        if nums[mid] == target:
            return True
        if nums[begin] <= nums[mid]:
            if nums[begin] <= target & target <= nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            if nums[mid] <= target & target <= nums[end]:
                begin = mid + 1
            else:
                end = mid - 1
    return False


nums = [4, 5, 6, 7, 1, 2, 3]

print(search(nums, 7))
