# 문제 : DFS와 BFS(실버2)
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1
```python
4 5 1
1 2
1 3
1 4
2 4
3 4
```
# 예제 출력1
```python
1 2 4 3
1 2 3 4
````

# 구현 알고리즘
```python
import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)] # 탐색 돌릴 그래프 생성

visited = [False for _ in range(n+1)] # 방문 유무를 나타내는 list 생성

def dfs(graph,visited,v): # dfs
    visited[v] = True # 방문했으므로 True
    print(v,end=' ') # 방문한 경로 출력
    for i in graph[v]: # v와 간선으로 연결된 정점들 돌면서
        if visited[i] == False: # 방문을 아직 안한경우
          dfs(graph,visited,i) # 재귀함수 이용해서 방문 안한곳 방문시키기


def bfs(visited,start): # bfs
    queue = deque([start]) # queue 이용
    visited[start] = True # 방문했으므로 True

    while queue: # queue가 비어있지 않을때까지 반복
        num = queue.popleft() # queue의 맨밑에값(맨 왼쪽)값 제거후 뽑아
        print(num,end=' ') # 출력
        for i in graph[num]: # queue에서 뽑은 값과 간선으로 연결된 정점들 돌면서
            if visited[i] == False: # 방문을 아직 안한 경우
                visited[i] = True # 방문을 해주고 True 
                queue.append(i)# 방문한 곳 queue에 추가해주기


for i in range(m): # m번 돌아주면서
    a,b = map(int,sys.stdin.readline().rstrip().split()) # a,b값 즉 서로 간선으로 연결된 정점 입력 받으면서
    graph[a].append(b) # list형식으로 보기쉽게 정리 -> ex)1,2와1,3인 경우 [[],[2,3],[1],[1]]:index 0 부터 시작한다고 가정
    graph[b].append(a) # list형식으로 보기쉽게 정리

[num.sort() for num in graph] # sort를 사용해서 먼저 크기순으로 정렬해준다. [[2,1,3]] -> [[1,2,3]]

dfs(graph,visited,v) # dfs 시작, 굳이 graph,visited,v 넣어줄 필요는 없다.
visited = [False for _ in range(n+1)] # dfs 실행하고, bfs 실행시키기 위해서는 visited 리스트 초기화 해주어야 한다.
print() # 출력시 한칸 띄워주고
bfs(visited,v) # bfs 시작
```
