# 문제 : 회전하는 큐(실버IV)

지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

# 출력
첫째 줄에 문제의 정답을 출력한다

# 예제 입력 1
```python
  10 3
  1 2 3
```

# 에제 출력 1
```python
  0
```

# 구현 알고리즘

```python
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split()) # 큐의 크기, 뽑아내려가 하는 수의 개수 입력
values = list(map(int,input().split())) # 값들 받아오기
answer = 0 # 정답
array = deque([i for i in range(1,n+1)]) # 1부터 n까지 원소를 가진 deque 생성

for value in values: 각 원소들을 탐방하며
    while True: # 무한 반복
        if value == array[0]: # 맨 앞 원소와 value가 같다면
            array.popleft() # 맨 앞의 원소 제거
            break # 반복문 탈출
        else: # 그렇지 않다면
            if array.index(value)<=len(array)//2: # array의 길이의 절반값보다 값의 index 값이 작거나 같다면
                array.rotate(-1) # 왼쪽으로 한칸씩 땡겨
            else: # 그렇지 않다면
                array.rotate(1) # 오른쪽으로 한칸씩 땡겨
            answer+=1 # answer에 + 1 -> 왜? 왼쪽, 오른쪽 땡겨주는 경우 2,3번을 수행했기 때문에

print(answer) # 결과 출력
```

# 풀이 과정
![KakaoTalk_Photo_2022-01-27-14-31-30](https://user-images.githubusercontent.com/69062776/151297733-3481a676-ad1a-42fb-a763-054ceeaa1f64.jpeg)
