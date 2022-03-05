import sys

n = int(sys.stdin.readline().rstrip())
res = 0

for i in range(1,n+1):
    number = list(str(i))
    number = list(map(int,number))
    
    if n == i+sum(number):
        res = i
        break

print(res)