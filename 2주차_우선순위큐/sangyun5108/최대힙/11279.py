import heapq
import sys

n = int(sys.stdin.readline().rstrip())

heap = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-num,num))