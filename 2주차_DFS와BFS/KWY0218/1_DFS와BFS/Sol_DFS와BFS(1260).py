import sys
from collections import deque

'''
    1. 크기가 N인 visited 리스트를 만든다.
    2. 출발노드에 하위 노드들이 있는지 검사한 후 dfs를 진행한다. <- 출발노드가 [] 일 때를 위해
    3. dfs가 끝난 후 다른 정점이 있는지 확인한 후, 있으면 다시 dfs를 진행한다. <- 정점이 여러개일 때를 위해
    visited의 index는 (0<=index<=N-1) 이므로 방문할 때 index-1 을 한다.
    stack.extend(sorted(site[index],reverse=True)) 한 이유 : 1:[3,2,4]일 때 [4,3,2] 순서대로 append 해야 [2,3,4] 순서대로 pop할 수 있기 때문에
'''
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

    for i in range(1,size+1):
        if not visited[i-1] and site[i]:
            stack.append(i)
            while stack:
                index = stack.pop()
                if not visited[index-1]:
                    visited[index-1] = True
                    stack.extend(sorted(site[index],reverse=True))
                    answer.append(index)
                        
    for i in answer: print(i,end=" ")

'''
    1. 크기가 N인 visited 리스트를 만든다.
    2. 출발노드에 하위 노드들이 있는지 검사한 후 bfs를 진행한다. <- 출발노드가 [] 일 때를 위해
    3. bfs가 끝난 후 다른 정점이 있는지 확인한 후, 있으면 다시 bfs를 진행한다. <- 정점이 여러개일 때를 위해
    visited의 index는 (0<=index<=N-1) 이므로 방문할 때 index-1 을 한다.
    que.extend(sorted(site[index])) sorted를 한 이유 : 1:[3,2,4]일 때 [2,3,4] 순서대로 append 해야 [2,3,4] 순서대로 popleft 할 수 있기 때문에
'''   
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

    for i in range(1,size+1):
        if not visited[i-1] and site[i]:
            que.append(i)
            while que:
                index = que.popleft()
                if not visited[index-1]:
                    visited[index-1] = True
                    que.extend(sorted(site[index]))
                    answer.append(index)
                        
    for i in answer: print(i,end=" ")

'''
    양방향 그래프이므로 head와 tail, tail과 head 모두 연결한다.
'''
N,M,V = list(map(int,sys.stdin.readline().rstrip().split(" ")))
site = dict()
for i in range(1,N+1): site[i] = []
for _ in range(M):
    head, tail = map(int,sys.stdin.readline().rstrip().split(" "))
    site[head].append(tail)
    site[tail].append(head)

dfs(site,N,V)
print()
bfs(site,N,V)
