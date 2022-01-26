import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    n,m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    answer = 0

    while queue:
        max_value = max(queue)
        first = queue.popleft()
        m -= 1

        if max_value != first:
            queue.append(first)
            if m < 0: # -1인 경우
                m = len(queue)-1
        else:
            answer+=1
            if m == -1:
                print(answer)
                break
