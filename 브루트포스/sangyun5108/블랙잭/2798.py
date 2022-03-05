import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

number = list(map(int,sys.stdin.readline().rstrip().split()))

answer = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = number[i]+number[j]+number[k]
            if sum<=m and sum>answer:
                answer = sum

print(answer)