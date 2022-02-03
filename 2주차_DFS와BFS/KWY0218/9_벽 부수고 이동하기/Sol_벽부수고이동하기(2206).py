import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split(" "))
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
site = deque([[0,0,True]])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while site:
    x,y,isCrash = site.popleft()
    print("x:{0}, y:{1}, isCrash:{2}".format(x,y,isCrash))
    for i in range(4):
        r = x-dx[i]
        c = y-dy[i]
        if 0<=r<M and 0<=c<N and graph[c][r]==0:
            graph[c][r] = graph[y][x] + 1
            site.append([r,c,isCrash])
        elif isCrash and 0<=r<M and 0<=c<N and graph[c][r]==1:
            graph[c][r] = graph[y][x] + 1
            site.append([r,c,False])

answer = True
for c in graph:
    for r in c:
        if r == 0: 
            answer = False
            break
print(graph)
print(graph[N-1][M-1]+1) if answer else print(-1)