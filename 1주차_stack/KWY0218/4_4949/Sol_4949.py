import sys

def Solution(s:str):
    operatorMap = {"[":"]","(":")"}
    stack = []
    for i in S:
        if i in operatorMap.keys():
            stack.append(i)
        elif i in operatorMap.values():
            if not stack or operatorMap[stack.pop()]!=i: return False
    return False if stack else True

while True:
    S = list(sys.stdin.readline().rstrip())
    if S[0] ==".": break
    print("yes") if Solution(S) else print("no")