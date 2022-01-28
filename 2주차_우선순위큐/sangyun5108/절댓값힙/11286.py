import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
numbers = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    numbers.append(num)

    if num<0: # 절댓값 만들어주기
        num*=-1

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            result = heapq.heappop(heap)
            rev = -1*result
            if rev in numbers:
                print(rev)
                numbers.remove(rev)
            else:
                print(result)

    
    else:
        heapq.heappush(heap,num)
        
