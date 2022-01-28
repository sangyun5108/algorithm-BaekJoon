# 문제 : 절댓값 힙(실버I)
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

# 출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 예제 입력 1
```python
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
```

# 예제 출력1

```python
-1
1
0
-1
-1
1
1
-2
2
0
```

# 구현 알고리즘
```python
import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = [] # 절댓값을 취한 숫자들을 담을 리스트
numbers = [] # 원래 숫자들을 담을 리스트

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    numbers.append(num) # 원본을 담아준다

    if num<0: # 절댓값 만들어주기 # 0보다 작으면 
        num*=-1 # 절댓값을 만들어준다

    if num == 0: # num이 0인경우
        if len(heap) == 0: # heap 길이가 0이라면
            print(0) # 0 출력
        else: # heap 길이가 0이 아니라면
            result = heapq.heappop(heap) # heap에서 제일 작은 수 제거후 변수에 담아준다.
            rev = -1*result # -1을 곱한수를 rev 변수에 담아준다
            if rev in numbers: # 만약 -1을 곱하 수가 numbers 즉 원본 숫자에 포함이 되어있다면
                print(rev) # -1을 곱한수를 출력해주고
                numbers.remove(rev) # -1을 곱한수를 원본 배열에서 제거해준다 -> 1,-1인 경우 -1,-1 출력을 방지하기 위해
            else: # 그렇지 않으면
                print(result) # 그냥 result 값 출력
    else: # num이 0이 아닌경우
        heapq.heappush(heap,num) # heap에 num을 넣어준다
```
