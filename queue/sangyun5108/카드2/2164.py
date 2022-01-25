import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque([num+1 for num in range(n)])

change = 0

while True:
    if len(queue) == 1:
        break
    
    if change == 1:
        n = queue.popleft()
        queue.append(n)
        change = 0
    else:
        queue.popleft()
        change = 1

print(queue[0])
