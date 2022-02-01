import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 위,오,아,왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = []

def bfs(x,y):
    count = 1
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue 

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count+=1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

result.sort()

print(len(result))

for i in result:
    print(i)
