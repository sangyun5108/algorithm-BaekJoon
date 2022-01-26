import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
values = list(map(int,input().split()))
answer = 0
array = deque([i for i in range(1,n+1)])

for value in values:
    while True:
        if value == array[0]:
            array.popleft()
            break
        else:
            if array.index(value)<=len(array)//2:
                array.rotate(-1)
            else:
                array.rotate(1)
            answer+=1

print(answer)