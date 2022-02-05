# 문제 : 유기농 배추
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

![스크린샷 2022-02-05 오후 1 50 51](https://user-images.githubusercontent.com/69062776/152629376-be1e2458-a628-4dd9-a43b-12cde7c263c6.png)

# 입력

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

# 출력

각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

# 예제 입력1
```python
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
```
# 예제 출력1
```python
5
1
```
# 구현 알고리즘
```python
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip()) # 테스트 케이스 입력


def bfs(graph,x,y): 
    graph[x][y] = 0 # 파라미터로 전달 받은 좌표를 방문후, 1을 0으로 변경
    queue = deque() # queue 생성
    queue.append([x,y]) # queue에 x,y좌표 추가

    while queue: # queue가 빌때 까지
        x,y = queue.popleft() # x,y를 뽑아낸다.
        for i in range(4): # 이동방향을 돌면서
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n: # graph 범위를 벗어나면
                continue # for문 넘겨
            
            if graph[nx][ny] == 1: # graph가 1인경우 -> 유기농 배추가 있는 경우
                graph[nx][ny] = 0 # 방문을 했으므로 0으로 변경
                queue.append([nx,ny]) # nx,ny를 queue에 추가한다.

# 위,오,왼,아
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(T): # 테스트 케이스 for문 돌린다.
    m,n,k = map(int,sys.stdin.readline().rstrip().split())
    graph = [[0]*n for _ in range(m)] # graph를 생성 (테스트 경우 마다 다른 그래프를 생성)
    cnt = 0

    for j in range(k):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        graph[x][y] = 1 # 배추가 심어져 있는 위치를 그래프에 넣어준다,
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1: # 그래프에 배추가 심어져 있으면
                bfs(graph,i,j) # 배추가 심어저 있는 묶음을 찾기위해 bfs 탐색
                cnt += 1 # 탐색이 끝나면 이웃한 배추들을 묶는 묶음 갯수를 추가한다.
    print(cnt) # 갯수 출력

```
