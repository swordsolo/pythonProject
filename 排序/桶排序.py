# *_*coding:utf-8 *_*
# author:jijian
def radixSort(nums):
    """
    基数排序，数组元素必须是正整数
    >>>nums = [334, 5, 67, 345, 7, 99, 4, 23, 78, 45, 1, 3453, 23424]
    >>>radixSort(nums)
    >>>[1, 4, 5, 7, 23, 45, 67, 78, 99, 334, 345, 3453, 23424]
    """
    # 遍历数组获取数组最大值和最大值对应的位数
    # nums = [334, 5, 67, 345, 7, 99, 4, 23, 78, 45, 1, 3453, 23424]
    maxvalue = max(nums)
    # print maxvalue
    itercount = len(str(maxvalue))
    for i in range(itercount):
        bucket = [[] for _ in range(10)]  # 创建10个桶
        # 尾数相同的放在同一个桶里
        for num in nums:
            index = (num // 10 ** i) % 10
            print(num,index)
            bucket[index].append(num)
            print(bucket)
        # 清空原先的数组
        nums = []
        for b in bucket:
            nums.extend(b)
        print(nums)
    return nums


nums = [334, 5, 67, 345, 7, 99, 4, 23, 78, 45, 1, 3453, 23424]
radixSort(nums)
