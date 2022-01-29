import sys
import heapq

n = int(sys.stdin.readline().rstrip())

leftHeap = []
rightHeap = []
result = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap,(-num,num))
    else:
        heapq.heappush(rightHeap,num)
    
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap,(-min,min))
        heapq.heappush(rightHeap,max)
    
    result.append(leftHeap[0][1])
for j in result:
    print(j)

