import sys
import heapq

N = int(sys.stdin.readline().rstrip())
minheap = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        if len(minheap) == 0: print("0")
        else: print(heapq.heappop(minheap))
    else:
        heapq.heappush(minheap,n)