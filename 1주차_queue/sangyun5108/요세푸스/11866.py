import sys

input =  sys.stdin.readline
n,k = map(int,input().split())
numbers = [i for i in range(1,n+1)]
result = []
num = 0

for i in range(n):
    num += k-1
    if num>=len(numbers):
        num = num%len(numbers)
    
    result.append(str(numbers.pop(num)))

print("<",", ".join(result)[:],">",sep='')

