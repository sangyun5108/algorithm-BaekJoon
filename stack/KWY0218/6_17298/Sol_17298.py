import sys

N = int(sys.stdin.readline().rstrip())
sequenceList = list(map(int,sys.stdin.readline().rstrip().split()))
answer = []
tempList = []

index = N-1
while index>-1:
    if not tempList:
        answer.append(-1)
        tempList.append(sequenceList[index])
        index -= 1
    else:
        if tempList[-1] > sequenceList[index]:
            answer.append(tempList[-1])
            tempList.append(sequenceList[index])
            index -= 1
        else:
            tempList.pop()
            
for i in range(N-1,-1,-1):
    print(answer[i],end=" ")
print()