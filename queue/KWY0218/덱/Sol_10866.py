import sys

class Node:
    def __init__(self,item,next=None,prev=None) -> None:
        self.item = item
        self.next = next
        self.prev = prev

class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self,item):
        newNode = Node(item)
        if not self.head:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode
        self.size += 1
    
    def push_back(self,item):
        newNode = Node(item)
        if not self.head:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1   
    
    def pop_front(self):
        if not self.head: return -1
        temp = self.head.item
        self.head = self.head.next
        if not self.head: self.tail = None
        else: self.head.prev = None
        self.size -= 1
        return temp
    
    def pop_back(self):
        if not self.head: return -1
        temp = self.tail.item
        self.tail = self.tail.prev
        if not self.tail: self.head = None
        else: self.tail.next = None
        self.size -= 1
        return temp 
    
    def deque_size(self):
        return self.size
    
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
    if command[0] == "push_front":
        S.push_front(int(command[1]))
    elif command[0] == "push_back":
        S.push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(S.pop_front())
    elif command[0] == "pop_back":
        print(S.pop_back())
    elif command[0] == "size":
        print(S.deque_size())
    elif command[0] == "empty":
        print(S.empty())
    elif command[0] == "front":
        print(S.front())
    elif command[0] == "back":
        print(S.back())