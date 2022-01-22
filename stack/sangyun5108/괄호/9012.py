import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    values = list(input())
    result = 0

    for i in values:
        if i == '(':
            result+=1
        elif i == ')':
            result-= 1
        if result < 0:
            print('NO')
            break

    if result > 0 :
        print('NO')
    elif result == 0:
        print('YES')
