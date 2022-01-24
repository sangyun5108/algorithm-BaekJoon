n = int(input())

stack = []
answer = []
current = 1
right = 0

for i in range(n):
    num = int(input())

    while(current<=num):
        stack.append(current)
        current+=1
        answer.append('+')
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        right = 1
        break

if right == 0 :
    for i in answer:
        print(i)