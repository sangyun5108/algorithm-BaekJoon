import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

def dfs(graph,visited,v):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if visited[i] == False:
          dfs(graph,visited,i)


def bfs(visited,start):
    queue = deque([start])
    visited[start] = True

    while queue:
        num = queue.popleft()
        print(num,end=' ')
        for i in graph[num]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

[num.sort() for num in graph]

dfs(graph,visited,v)
visited = [False for _ in range(n+1)]
print()
bfs(visited,v)
