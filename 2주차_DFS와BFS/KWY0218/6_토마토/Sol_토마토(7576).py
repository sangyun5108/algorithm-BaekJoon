import sys
from collections import deque

M,N = map(int,sys.stdin.readline().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

site = deque()
count = 0
s = sum([sum(i) for i in graph])
if s == -(M*N): print(-1)
elif s == M*N: print(0)
else:
    for col in range(N):
        for row in range(M):
            if graph[col][row] == 1:
                site.append([col,row])
            if graph[col][row] == 1 or graph[col][row] == -1: count += 1
    if count == M*N: print(0)
    else:
        while site:
            y,x = site.popleft()
            if x-1>-1 and graph[y][x-1] == 0:
                graph[y][x-1] = graph[y][x]+1
                site.append([y,x-1])
            if x+1<M and graph[y][x+1] == 0:
                graph[y][x+1] = graph[y][x]+1
                site.append([y,x+1])
            if y-1>-1 and graph[y-1][x] == 0:
                graph[y-1][x] = graph[y][x]+1
                site.append([y-1,x])
            if y+1<N and graph[y+1][x] == 0:
                graph[y+1][x] = graph[y][x]+1
                site.append([y+1,x])
                
        answer = True
        for c in graph:
            for r in c:
                if r == 0:
                    answer = False
                    break
        print(max(max(i) for i in graph)-1) if answer else print(-1)