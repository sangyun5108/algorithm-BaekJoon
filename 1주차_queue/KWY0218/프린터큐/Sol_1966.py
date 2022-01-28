import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    NM = list(map(int,sys.stdin.readline().rstrip().split()))
    W = deque(list(map(int,sys.stdin.readline().rstrip().split())))
    indexW = deque([i for i in range(NM[0])])
    count = 0
    while True:
        if max(W) != W[0]:
            W.append(W.popleft())
            indexW.append(indexW.popleft())
        else:
            count += 1
            if indexW[0] == NM[1]:
                break
            W.popleft()
            indexW.popleft()
            
    print(count)