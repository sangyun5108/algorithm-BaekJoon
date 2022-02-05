# 문제 : 미로 탐색(실버 1)
N×M크기의 배열로 표현되는 미로가 있다.
![스크린샷 2022-02-05 오후 2 16 04](https://user-images.githubusercontent.com/69062776/152629700-8e6c5efc-d16c-4341-88ec-794a5c876d00.png)
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력1
```python
4 6
101111
101010
101011
111011
```
# 예제 출력 1
```python
15
```

# 구현 알고리즘
```python
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
            
            if graph[nx][ny] == 1: # 미로가 이동할 수 있는 곳이라면
                graph[nx][ny] = graph[x][y]+1 # 이동후에 이동한 횟수를 graph에 추가해준다.
                queue.append([nx,ny]) # queue에 nx,ny(그래프에 이동이 가능한 정점을 추가)

dfs(0,0) # 0,0부터 시작

print(graph[n-1][m-1]+1) # 도착지점에 적혀있는 graph의 값을 출력해준다.(이동환 횟수가 출력된다)
```
