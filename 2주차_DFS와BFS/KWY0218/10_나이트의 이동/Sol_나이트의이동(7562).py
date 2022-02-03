import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    I = int(sys.stdin.readline().rstrip())
    visited = [[False]*I for _ in range(I)]
    startingPoint = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    destination = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    
    que = deque([])
    startingPoint.append(0)
    que.append(startingPoint)
    
    while que:
        xSite,ySite,depth = que.popleft()
        if xSite == destination[0] and ySite == destination[1]: 
            print(depth) 
            break
        siteList = [
            [xSite-1,ySite-2,depth+1],
            [xSite+1,ySite-2,depth+1],
            [xSite+2,ySite-1,depth+1],
            [xSite+2,ySite+1,depth+1],
            [xSite-1,ySite+2,depth+1],
            [xSite+1,ySite+2,depth+1],
            [xSite-2,ySite-1,depth+1],
            [xSite-2,ySite+1,depth+1]
            ]
        for s in siteList:
            if 0<=s[0]<I and 0<=s[1]<I and not visited[s[1]][s[0]]: 
                que.append(s)
                visited[s[1]][s[0]] = True