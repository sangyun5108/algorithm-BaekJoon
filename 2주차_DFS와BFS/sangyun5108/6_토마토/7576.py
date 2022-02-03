import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())

# n : 가로
# m : 세로

graph = []

for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 위,오,아,왼

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i,j])
bfs()

result = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))

print(result-1)