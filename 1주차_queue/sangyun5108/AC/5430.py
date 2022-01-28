import sys
from collections import deque

test_case = int(input())

for i in range(test_case):
    orders = sys.stdin.readline().rstrip()
    n = int(input())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    flag = 0
    rev = 0

    if n == 0:
        queue = []
    
    for order in orders:
        if order == 'R':
            rev+=1
        elif order == 'D':
            if len(queue) < 1:
                print('error')
                flag = 1
                break
            else:
                if rev%2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    
    if flag == 0:
        if rev%2 == 0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")