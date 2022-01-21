import sys
class Solution:
    def __init__(self) -> None:
        self.stack = []
    
    def __len__(self):
        return len(self.stack)
    
    def isEmpty(self):
        return 1 if len(self.stack) == 0 else 0
    
    def top(self):
        return self.stack[-1] if not self.isEmpty() else -1
    
    def push(self,inteager):
        self.stack.append(inteager)
    
    def pop(self):
        return self.stack.pop() if self.stack else -1
    
# S =Solution()
# N = int(input())
# for i in range(N):
#     command = sys.stdin.readline().split()
#     if command[0] == "push":
#         S.push(command[1])
#     elif command[0] == "pop":
#         print(S.pop())
#     elif command[0] == "size":
#         print(len(S))
#     elif command[0] == "empty":
#         print(S.isEmpty())
#     elif command[0] == "top":
#         print(S.top())