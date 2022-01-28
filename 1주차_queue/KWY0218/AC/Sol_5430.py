import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    order = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    L = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    
    reverse = True
    answer = True
    for j in order:
        if j == 'R':
            reverse = not reverse
        else:
            if len(L) == 0 or L[0]=='':
                answer = False
                break
            if reverse:
                L.popleft()
            else:
                L.pop()
    if not answer: print("error")
    else:
        print("["+",".join(L)+"]") if reverse else print("["+",".join(reversed(L))+"]")