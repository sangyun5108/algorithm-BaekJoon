# 문제 : 단지번호붙이기(실버1)
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![스크린샷 2022-02-05 오후 1 43 32](https://user-images.githubusercontent.com/69062776/152628987-b1654a73-67d6-4505-a4bb-0c78858c5aca.png)

# 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 예제 입력1
```python
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```
# 예제 출력
```python
3
7
8
9
```
# 구현 알고리즘
```python
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 상,우,하,좌
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

            if nx<0 or nx>=n or ny<0 or ny>=n: # graph의 범위를 넘은 경은 경우
                continue # continue를 통해서 넘어간다.

            if graph[nx][ny] == 1: # graph의 값이 1인경우 -> 아파트가 있는 경우
                graph[nx][ny] = 0 # 방문을 하고, 0으로 만들어준다.
                queue.append((nx,ny)) # 아파트가 있던 정점을 추가해준다.
                count+=1 # 아파트 갯수를 추가해준다.
    return count # 단지내 아파트 갯수를 반환해준다.

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 만약 1인 아파트가 있다면
            result.append(bfs(i,j)) # 아파트를 통해 단지를 유추하기 위한 bfs 탐색

result.sort() # 단지내 갯수를 정렬해준다.

print(len(result)) # 단지의 갯수를 출력해준다.

for i in result: # 아파트 갯수를 출력해준다.
    print(i)

```
