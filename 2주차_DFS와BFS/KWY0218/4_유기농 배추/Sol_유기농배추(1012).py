import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    M,N,K = map(int,sys.stdin.readline().rstrip().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for i in range(K):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        field[y][x] = 1
        
    stack = []
    count = 0
    for col in range(N):
        for row in range(M):
            if not visited[col][row] and field[col][row] == 1:
                stack.append([col,row])
                while stack:
                    y,x = stack.pop()
                    visited[y][x] = True
                    if x+1<M and field[y][x+1] == 1 and not visited[y][x+1]:
                        if [y,x+1] not in stack: stack.append([y,x+1])
                    if x-1>-1 and field[y][x-1] == 1 and not visited[y][x-1]:
                        if [y,x-1] not in stack: stack.append([y,x-1])
                    if y+1<N and field[y+1][x] == 1 and not visited[y+1][x]:
                        if [y+1,x] not in stack: stack.append([y+1,x])
                    if y-1>-1 and field[y-1][x] == 1 and not visited[y-1][x]:
                        if [y-1,x] not in stack: stack.append([y-1,x])
                count += 1
    print(count)