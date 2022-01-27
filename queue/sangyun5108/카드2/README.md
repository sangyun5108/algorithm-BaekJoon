# 문제 : 카드 2(실버IV)
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

# 출력
첫째 줄에 남게 되는 카드의 번호를 출력한다.

# 구현 알고리즘

```python
import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # n 입력

queue = deque([num+1 for num in range(n)]) # 1부터 n까지 queue 생성

change = 0 # 조건을 컨트롤 하는 변수

while True: # 무한 반복
    if len(queue) == 1: # 길이가 1인경우 즉, 원소가 1개가 남은 경우
        break # 반복문 탈출
    
    if change == 1: # change가 1인 경우
        n = queue.popleft() # queue에서 제일 앞쪽 숫자 제거
        queue.append(n) # queue에서 맨 앞 숫자를 맨 뒤에 추가
        change = 0 # change 0으로 변경
    else: # change가 1이 아니면
        queue.popleft() # queue의 앞쪽에서 숫자 제거
        change = 1 # change를 1로 변경

print(queue[0])
```
- change라는 변수를 두어 두 조건이 번갈아서 수행되도록 구현하였다.
