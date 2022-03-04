import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

coins = []

for i in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)

result = 0

for i in coins:
    if i <= k:
        result += k//i
        k = k%i


print(result)
