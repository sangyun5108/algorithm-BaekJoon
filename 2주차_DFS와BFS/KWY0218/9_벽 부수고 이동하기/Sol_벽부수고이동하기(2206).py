import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split(" "))
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0,0]*2 for _ in range(M)] for _ in range(N)]
site = deque([[0,0,0]])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while site:
    x,y,isCrash = site.popleft()
    visited[y][x][isCrash] = 1
    for i in range(4):
        r = x-dx[i]
        c = y-dy[i]
        if 0<=r<M and 0<=c<N and graph[c][r]==0:
            visited[c][r][isCrash] = visited[y][x][isCrash] + 1
            site.append([r,c,isCrash])
        elif 0<=r<M and 0<=c<N and isCrash==0 and graph[c][r]==1:
            visited[c][r][isCrash+1] = visited[y][x][isCrash] + 1
            site.append([r,c,isCrash])

answer = True
for c in graph:
    for r in c:
        if r == 0: 
            answer = False
            break
print(graph)
print(graph[N-1][M-1]+1) if answer else print(-1)