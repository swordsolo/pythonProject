# *_*coding:utf-8 *_*
# author:jijian

#选择排序
list=[49,38,97,76,65,13,27,50]
count=len(list)
for i in range(count):
    min =i
    for j in range(i+1,count):
        if list[min]>list[j]:
            min=j
    list[min],list[i]=list[i],list[min]
print(list)

#插入排序
list=[49,38,97,76,65,13,27,50]
count=len(list)
for i in range(1,count):
    key=list[i]
    j=i-1
    while j>=0:
        if list[j]>list[j+1]:
            list[j+1]=list[j]
            list[j]=key
        j-=1
print(list)

#插入排序2
list=[49,38,97,76,65,13,27,50]
count=len(list)
for i in range(1,count):
    key=list[i]
    j=i-1
    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key

print(list)

#插入排序3
list=[49,38,97,76,65,13,27,50]
count=len(list)
for i in range(0,count):
    for j in range(i-1,-1,-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)


##归并排序
def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(list):
    if len(list)<=1:
        return list
    num=len(list)/2
    left=merge_sort(list[:num])
    right=merge_sort(list[num:])
    return merge(left,right)

print(merge_sort(list))


#快速排序
list=[49,38,97,76,65,13,27,50]
def quick_sort(lists):
    if len(lists)<2:
        return lists
    pivot=lists[0]
    greater=[i for i in lists[1:] if i>=pivot]
    less=[i for i in lists[1:] if i<pivot]
    #return quick_sort(less)
    return quick_sort(less)+[pivot]+quick_sort(greater)


print(quick_sort(list))