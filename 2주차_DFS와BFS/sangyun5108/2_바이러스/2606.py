import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]

result = 0

def dfs(visited,v):
    global result
    visited[v] = True
    result+=1
    for i in graph[v]:
        if visited[i] == False:
            dfs(visited,i)

dfs(visited,1)

print(result-1)
        
