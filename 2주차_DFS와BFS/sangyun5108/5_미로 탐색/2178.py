import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    graph[x][y] = 0
    queue = deque()
    queue.append(deque([x,y]))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])

dfs(0,0)

print(graph[n-1][m-1]+1)