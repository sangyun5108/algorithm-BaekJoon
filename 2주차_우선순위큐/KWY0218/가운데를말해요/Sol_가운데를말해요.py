import sys
import heapq

N = int(sys.stdin.readline().rstrip())
maxHeap = []
minHeap = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())

    if len(maxHeap)==0 or maxHeap[0][1]>n: heapq.heappush(maxHeap,(-n,n))
    elif len(minHeap)==0 or minHeap[0]<n: heapq.heappush(minHeap,n)
    else: heapq.heappush(maxHeap,(-n,n))
    
    if len(maxHeap) - len(minHeap) == -2: 
        minData = heapq.heappop(minHeap)
        heapq.heappush(maxHeap,(-minData,minData))
    elif len(maxHeap) - len(minHeap) == 2:
        heapq.heappush(minHeap, heapq.heappop(maxHeap)[1]) 
    
    length = len(maxHeap) + len(minHeap)
    if length%2==1: print(maxHeap[0][1]) if len(maxHeap)>len(minHeap) else print(minHeap[0])
    else: print(maxHeap[0][1]) if maxHeap[0][1]<minHeap[0] else print(minHeap[0])