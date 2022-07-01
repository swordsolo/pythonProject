# *_*coding:utf-8 *_*
# author:jijiana
import time
list=[i for i in range(1,101)]
n=len(list)
count=0
front=0
rear=n-1
start1=time.time()
for i in range(n):
   for j in range(i+1,n):
       for k in range(j+1,n):
           if list[i]+list[j]>list[k]:
               print([list[i],list[j],list[k]])
               count+=1
print list
end1=time.time()
start2=time.time()

for i in range(n-1):
    # print "i==",i
    tail=n-1
    front=tail-1
    while tail-1>i:
        if front>i and list[i]+list[front]>list[tail]:
            print([list[i],list[front],list[tail]])
            front-=1
            count+=1
        else:
            tail-=1
            front=tail-1
end2=time.time()
diff1=end1-start1
diff2=end2-start2
print start1,end1
print start2,end2
print diff1,diff2
print(count)
