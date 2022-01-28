import sys

N = int(sys.stdin.readline().rstrip())
goalStack = []
for i in range(N):
    goalStack.append(int(sys.stdin.readline().rstrip()))

stack = []
answer = []
index = 0
inteager = 1
while inteager<=N:
    if stack and stack[-1] == goalStack[index]:
        answer.append("-")
        stack.pop()
        index += 1
    else:
        stack.append(inteager)
        answer.append("+")
        inteager += 1
        
while index<N:
    if stack[-1] == goalStack[index]:
        answer.append("-")
        stack.pop()
        index += 1
    else:
        break

if stack: print("NO")
else:
    for i in answer:
        print(i)