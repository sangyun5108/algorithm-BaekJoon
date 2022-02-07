import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    V,E = map(int,sys.stdin.readline().rstrip().split(" "))
    graph = dict()
    for i in range(1,V+1): graph[i] = []
    for _ in range(E):
        head, tail = map(int,sys.stdin.readline().rstrip().split(" "))
        graph[head].append(tail)
        graph[tail].append(head)
    visited = [False]*V
    print(graph)