import sys
import heapq

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers))
    else:
        heapq.heappush(numbers,num)
