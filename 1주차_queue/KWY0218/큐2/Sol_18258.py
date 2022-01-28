import sys

class Node:
    def __init__(self,item = 0,next = None,prev = None) -> None:
        self.item = item
        self.next = next
        self.prev = prev
        
class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
        
    def push(self,item:int):
        newNode = Node(item = item)
        if not self.head: self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1
    
    def pop(self):
        if not self.head: return -1
        temp = self.head.item
        self.head = self.head.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        self.size-=1
        return temp
    
    def empty(self):
        return 0 if self.head else 1
    
    def front(self):
        return self.head.item if self.head else -1
    
    def back(self):
        return self.tail.item if self.head else -1
    
S = Solution()
N = int(input())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        S.push(int(command[1]))
    elif command[0] == "pop":
        print(S.pop())
    elif command[0] == "size":
        print(len(S))
    elif command[0] == "empty":
        print(S.empty())
    elif command[0] == "front":
        print(S.front())
    elif command[0] == "back":
        print(S.back())