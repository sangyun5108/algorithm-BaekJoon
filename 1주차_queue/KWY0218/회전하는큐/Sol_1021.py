import sys
from collections import deque

NM = list(map(int,sys.stdin.readline().rstrip().split()))
C = list(map(int,sys.stdin.readline().rstrip().split()))

count = 0
sequenceList = deque([i for i in range(1,NM[0]+1)])
C.reverse()

while C:
    index = sequenceList.index(C[-1])
    while sequenceList[0] != C[-1]:
        if len(sequenceList)//2 >= index:
            sequenceList.append(sequenceList.popleft())
            count +=1
        else:
            sequenceList.appendleft(sequenceList.pop())
            count += 1
    C.pop()
    sequenceList.popleft()
print(count)