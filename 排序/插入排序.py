# *_*coding:utf-8 *_*
# author:jijian
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        low = 0
        high = i - 1
        while (low <= high):
            mid = (high + low) // 2
            if tmp < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        nums = nums[:low] + [tmp] + nums[low:i] + nums[i + 1:]
        print(nums)
    return nums


if __name__ == "__main__":
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insert_sort(nums))