import sys
from collections import deque

n,k = map(int,sys.stdin.readline().rstrip().split())

queue = deque()
queue.append(n)

MAX = 100000

graph = [0]*(MAX+1)

def bfs():
    while queue:
        pop_num = queue.popleft()
        if pop_num == k:
            break
        for i in (pop_num+1,pop_num-1,2*pop_num):
            if 0<=i<=MAX and graph[i] == 0:
                graph[i] = graph[pop_num]+1
                queue.append(i)

bfs()

print(graph[k])