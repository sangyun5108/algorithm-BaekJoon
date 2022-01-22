# 문제 : 스택  (실버4)
### 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성

명령 종류
- push X : 정수 X를 스택에 넣는 연산
- pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력, 스택에 들어있는 정수가 없을땐 -1 출력
- size : 스택에 들어있는 정수의 개수 출력
- empty : 스택이 비어있는경우 1, 아닌경우 0 출력
- top : 스택의 가장 위에 있는 정수를 출력, 스택에 수가 없는 경우 -1 출력

## 구현 알고리즘 
```python
import sys

input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):   # 입력받은 명령어 횟수만큼 반복
    command = input().split() # 명령어 입력

    if command[0] == 'push': # 명령어가 push인경우
        stack.append(command[1]) # stack에 두번째로 입력받은 값 넣어준다.
    elif command[0] == 'top': # 명령아가 top인경우
        if len(stack) == 0: # 길이가 0이면
            print(-1) # -1 출력
        else: # 그렇지 않으면
            print(stack[-1]) # stack의 맨 윗부분(맨뒤) 출력
    elif command[0] == 'size': # 명령어가 size 인 경우
        print(len(stack)) # stack 길이 출력
    elif command[0] == 'empty': # 명령어가 empty인 경우
        if len(stack) == 0: # 길이가 0인경우
            print(1) # 1 출력
        else: # 그렇지 않으면
            print(0) # 0 출력
    elif command[0] == 'pop': # 명령어가 pop인 경우
       if len(stack) == 0: # 길이가 0인경우
           print(-1) # -1 출력
       else: # 그렇지 않으면
           print(stack.pop()) # stack 맨위(맨뒤)의 수를 빼고 뺀값 출력
```
