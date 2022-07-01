# *_*coding:utf-8 *_*
# author:jijian
def quickSort(nums, left, right):
    if left > right:
        return nums
    key = nums[left]
    low = left
    high = right
    while left < right:
        while left < right and nums[right] > key:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < key:
            left += 1
        nums[right] = nums[left]
    nums[left] = key
    quickSort(nums, low, left - 1)
    quickSort(nums, left + 1, high)
    return nums


if __name__ == "__main__":
    nums = [8, 9, 7, 6, 5, 4, 3, 2, 1]
    n = len(nums)
    print(quickSort(nums, 0, n - 1))
