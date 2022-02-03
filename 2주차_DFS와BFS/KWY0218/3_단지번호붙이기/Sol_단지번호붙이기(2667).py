import sys

N = int(sys.stdin.readline().rstrip())
stack = []
visited = [[False]*N for _ in range(N)]
for i in range(N): stack.append(list(map(int,sys.stdin.readline().rstrip())))
s = []
answer = []

for col in range(N):
    for row in range(N):
        if not visited[col][row] and stack[col][row] == 1:
            count = 0
            s.append([col,row])
            while s:
                y,x = s.pop()
                visited[y][x] = True
                count += 1
                if x+1<N and stack[y][x+1] == 1 and not visited[y][x+1]:
                    if [y,x+1] not in s: s.append([y,x+1])
                if x-1>-1 and stack[y][x-1] == 1 and not visited[y][x-1]:
                    if [y,x-1] not in s: s.append([y,x-1])
                if y+1<N and stack[y+1][x] == 1 and not visited[y+1][x]:
                    if [y+1,x] not in s: s.append([y+1,x])
                if y-1>-1 and stack[y-1][x] == 1 and not visited[y-1][x]:
                    if [y-1,x] not in s: s.append([y-1,x])
            answer.append(count)
            
print(len(answer))
for i in sorted(answer): print(i)