import sys

n = int(sys.stdin.readline().rstrip())
roads = list(map(int,sys.stdin.readline().rstrip().split()))
costs = list(map(int,sys.stdin.readline().rstrip().split()))

m = costs[0]
res = 0
for i in range(n-1):

    if m>costs[i]:
        m = costs[i]

    res+=m*roads[i]

print(res)