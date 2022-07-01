# *_*coding:utf-8 *_*
# author:jijian
def quick_sort(lists):
    if len(lists) < 2:
        return lists
    pivot = lists[0]
    greater = [i for i in lists[1:] if i > pivot]
    less = [i for i in lists[1:] if i < pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quick_sort(lists))
