import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split(" "))
site = deque()
site.append([N,0])
visited = [False]*100001
while site:
    s,depth = site.popleft()
    if s==M:
        print(depth)
        break
    visited[s]=True
    for i in (s-1,s+1,2*s):
        if 0<= i <=100000 and not visited[i]: site.append([i,depth+1])