import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())


def bfs(graph,x,y):
    graph[x][y] = 0
    queue = deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx,ny])

# 위,오,왼,아
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(T):
    m,n,k = map(int,sys.stdin.readline().rstrip().split())
    graph = [[0]*n for _ in range(m)]
    cnt = 0

    for j in range(k):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt += 1
    print(cnt)
