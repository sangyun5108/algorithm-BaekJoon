import sys

n = int(sys.stdin.readline().rstrip())

list=[]
rank=[]

for i in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    list.append((x,y))

for i in range(n):
    count = 1
    for j in range(n):
        if list[i][0]<list[j][0] and list[i][1]<list[j][1]:
            count+=1
    rank.append(count)

for i in rank:
    print(i,end=' ')