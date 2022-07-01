# *_*coding:utf-8 *_*
# author:jijian

def maxLength(arr):
    # write code here
    from_pos = 0
    mp = {}
    n = len(arr)
    max_len = 0
    for i in range(n):
        print("i=",i)
        #print("------------")
        if arr[i] in mp:
            max_len = max(max_len, i - from_pos)
            pos = mp[arr[i]]
            print("pos=",pos)
            for j in range(from_pos, pos + 1):
                print(mp[arr[j]])
                del mp[arr[j]]
            from_pos = pos + 1
            print("------------")

        mp[arr[i]] = i
    max_len = max(max_len, n - from_pos)
    return max_len



w=maxLength([1,2,3,1,2,3,2,2])
print(w)

while len(list1)>1:
    n=len(list1)
    list_diff=[]
    for i in range(1,n):
        list_loop=[]
        if len(list[0])==len(list[i]) and list[0] in list[i]*2:
            list_loop.append(list1[i])
            list.remove(list1[i])


    list3.append(list2)
print(len(list3))
