import sys
from collections import deque

M,N,H = list(map(int,sys.stdin.readline().rstrip().split()))
graph = []
s = 0
for i in range(H):
    temp = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
    s += sum([sum(i) for i in temp])
    graph.append(temp)

if sum == N*M*H: print(0)
elif sum == -(N*M*H): print(-1)
else:
    site = deque()
    count = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 1:
                    site.append([h,n,m])
                if graph[h][n][m] == 1 or graph[h][n][m] == -1: count += 1
    if count == N*M*H: print(0)
    else:
        h = [-1,1,0,0,0,0]
        c = [0,0,0,0,-1,1]
        r = [0,0,-1,1,0,0]
        while site:
            height, col, row = site.popleft()
            for i in range(6):
                dh = height + h[i]
                dc = col+c[i]
                dr = row+r[i]
                if 0<=dh<H and 0<=dc<N and 0<=dr<M:
                    if graph[dh][dc][dr] == 0:
                        graph[dh][dc][dr] = graph[height][col][row]+1
                        site.append([dh,dc,dr])
        
        answer = True
        for z in graph:
            for y in z:
                for x in y:
                    if x == 0: 
                        answer = False
                        break
        
        print(max(max(max(i) for i in z) for z in graph)-1) if answer else print(-1)