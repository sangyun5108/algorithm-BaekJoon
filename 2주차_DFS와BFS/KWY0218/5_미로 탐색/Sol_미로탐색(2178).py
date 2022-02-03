import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split())
field = []
for _ in range(N):
    field.append(list(map(int,sys.stdin.readline().rstrip())))

que = deque()
count = 0
que.append([0,0])

while que:
    y,x = que.popleft()
    if x-1>-1 and field[y][x-1]==1:
        field[y][x-1] = field[y][x]+1
        que.append([y,x-1])
    if x+1<M and field[y][x+1]==1:
        field[y][x+1] = field[y][x]+1
        que.append([y,x+1])
    if y-1>-1 and field[y-1][x]==1:
        field[y-1][x] = field[y][x]+1
        que.append([y-1,x])
    if y+1<N and field[y+1][x]==1:
        field[y+1][x] = field[y][x]+1
        que.append([y+1,x])

print(field[N-1][M-1])

# import sys
# from collections import deque

# N,M = map(int,sys.stdin.readline().rstrip().split())
# field = []
# for _ in range(N):
#     field.append(list(map(int,sys.stdin.readline().rstrip())))

# que = deque()
# que.append([0,0])
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# while que:
#     y,x = que.popleft()
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<M and 0<=ny<N:
#             if field[ny][nx] == 1:
#                 field[ny][nx] = field[y][x]+1
#                 que.append([ny,nx])

# print(field[N-1][M-1])