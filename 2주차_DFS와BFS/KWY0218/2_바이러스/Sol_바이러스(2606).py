import sys

size = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
S = dict()
for i in range(1,size+1): S[i] = []

for i in range(N):
    head, tail = map(int,sys.stdin.readline().rstrip().split())
    S[head].append(tail)
    S[tail].append(head)
    
count = -1
stack = [1]
visited = [False]*size

while stack:
    index = stack.pop()
    if not visited[index-1]:
        stack.extend(S[index])
        visited[index-1] = True
        count += 1

print(count) if count != -1 else print(0)