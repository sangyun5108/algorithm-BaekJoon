import sys
from collections import deque

NK = list(map(int,sys.stdin.readline().rstrip().split()))
que = deque([i for i in range(1,NK[0]+1)])
answer = []

while que:
    for i in range(NK[1]-1):
        que.append(que.popleft())
    answer.append(que.popleft())

print("<",end="")
for i in range(len(answer)-1):
    print(answer[i],end=", ")
print(f"{answer[-1]}>")