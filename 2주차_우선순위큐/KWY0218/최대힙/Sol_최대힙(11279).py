import sys
import heapq

N = int(sys.stdin.readline().rstrip())
maxheap = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        if len(maxheap) == 0: print(0)
        else: print(heapq.heappop(maxheap)[1])
    else:
        heapq.heappush(maxheap,(-n,n))