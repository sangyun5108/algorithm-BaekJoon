# 문제 : 큐2(실버IV)
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 구현 알고리즘
```python
  import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input()) # 테스트 케이스 입력

queue = deque([]) # queue 생성

for i in range(test_case): # 테스트 케이스 값만큼 반복

    command = list(input().split()) 명령어 입력

    if command[0] == 'push': # 명령어가 push인 경우
        queue.append(command[1]) # 명령어 뒤에온 숫자 queue에 추가
    
    elif command[0] == 'pop': # 명령어가 pop인 경우
        if len(queue) == 0: # queue의 길이가 0인경우
            print('-1') # -1 출력
        else: # 그렇지 않으면
            print(queue.popleft()) # queue의 맨앞에서 숫자 제거
    
    elif command[0] == 'size': # 명령어가 size인 경우
        print(len(queue)) # queue의 길이 출력
    
    elif command[0] == 'empty': # 명령어가 empty인 경우
        if len(queue)==0: # queue의 길이가 0인경우
            print(1) # 1 출력
        else: # 그렇지 않으면
            print(0) # 0 출력
    elif command[0] == 'front': # 명령어가 front인 경우
        if len(queue)==0: # queue의 길이가 0인경우
            print(-1) # -1 출력
        else: # 그렇지 않으면
            print(queue[0]) # queue의 맨 앞에 숫자 출력
    elif command[0] == 'back': # 명령어가 back인 경우
        if len(queue)==0: # 길이가 0이면
            print(-1) # -1 출력
        else: # 그렇지 않으면
            print(queue[-1]) # queue의 맨 뒤에 숫자 출력
```
