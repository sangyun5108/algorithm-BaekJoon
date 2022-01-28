import sys

def Solution(s:str):
    stack = []
    s = list(s)
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack: stack.pop()
            else: return False
    return False if stack else True
            
N = int(sys.stdin.readline().strip())
for i in range(N):
    S = sys.stdin.readline().strip()
    print("YES") if Solution(S) else print("NO")