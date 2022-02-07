import sys
import heapq

N = int(sys.stdin.readline().rstrip())
minHeap = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        if len(minHeap) == 0: print(0)
        else: print(heapq.heappop(minHeap)[1])
    else:
        heapq.heappush(minHeap,(abs(n),n))