import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

answer = []

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-1,1,-1]

def bfs():
    while queue:
        x,y = queue.popleft()
        if x == a and y == b: #원하는 칸으로 이동
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])

for i in range(test_case):
    n = int(input().rstrip())
    x,y = map(int,input().rstrip().split())
    a,b = map(int,input().rstrip().split())
    graph = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append([x,y])
    bfs()
    answer.append(graph[a][b]) # 이동한 칸 수 저장

for i in answer:
    print(i)


