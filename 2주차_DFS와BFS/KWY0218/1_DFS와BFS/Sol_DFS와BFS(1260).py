import sys
from collections import deque

def dfs(site:dict,size:int,start:int):
    visited = [False]*size
    stack = []
    answer = []
    if site[start]:
        stack.append(start)
        while stack:
            index = stack.pop()
            if not visited[index-1]:
                visited[index-1] = True
                stack.extend(sorted(site[index],reverse=True))
                answer.append(index)

    # for i in range(1,size+1):
    #     if not visited[i-1] and site[i]:
    #         stack.append(i)
    #         while stack:
    #             index = stack.pop()
    #             if not visited[index-1]:
    #                 visited[index-1] = True
    #                 stack.extend(sorted(site[index],reverse=True))
    #                 answer.append(index)
                        
    for i in answer: print(i,end=" ")

def bfs(site:dict,size:int,start:int):
    visited = [False]*size
    que = deque([])
    answer = []
    if site[start]:
        que.append(start)
        while que:
            index = que.popleft()
            if not visited[index-1]:
                visited[index-1] = True
                que.extend(sorted(site[index]))
                answer.append(index)

    # for i in range(1,size+1):
    #     if not visited[i-1] and site[i]:
    #         que.append(i)
    #         while que:
    #             index = que.popleft()
    #             if not visited[index-1]:
    #                 visited[index-1] = True
    #                 que.extend(sorted(site[index]))
    #                 answer.append(index)
                        
    for i in answer: print(i,end=" ")

N,M,V = list(map(int,sys.stdin.readline().rstrip().split(" ")))
site = dict()
for i in range(1,N+1): site[i] = []
for _ in range(M):
    head, tail = map(int,sys.stdin.readline().rstrip().split(" "))
    site[head].append(tail)
    site[tail].append(head)

print(site)
dfs(site,N,V)
print()
bfs(site,N,V)
