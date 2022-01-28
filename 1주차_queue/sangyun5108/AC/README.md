# 문제 : AC(골드V)
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

# 출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

# 예제 입력 1
```python
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
```

# 예제 출력 1
```python
[2,1]
error
[1,2,3,5,8]
error
```
# 구현 알고리즘
```python
import sys
from collections import deque

test_case = int(input()) # test_case 입력

for i in range(test_case): # test_case 만큼 반복
    orders = sys.stdin.readline().rstrip() # 명령어 입력 / rstrip() : 오른쪽 공백을 제거한다.
    n = int(input()) # n 입력
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(",")) # [] 대괄호를 제거한 순수 값들로만 queue 생성
    flag = 0 # 정답 출력시 필요한 변수
    rev = 0 # reverse(역순)을 해줄지 말지에 대한 변수 / rev = 2 인 경우는 그대로 이므로 굳이 queue.reverse()해줄 필요가 없다 : 시간 낭비 줄이기

    if n == 0: # n == 0 인경우
        queue = [] # queue를 빈배열로 초기화 왜? deque([])는 길이가 1이된다.
    
    for order in orders: # 각 order를 실행하기 위한 반복문
        if order == 'R': # order가 R인 경우
            rev+=1 # rev + 1 
        elif order == 'D': # order가 D인 경우
            if len(queue) < 1: # 길이가 1보다 작다면
                print('error') # 에러 출력
                flag = 1 # flag 를 1로 초기화
                break # 반복문 탈출 : 더이상 볼 필요가 없다
            else: # 그렇지 않다면
                if rev%2 == 0: # 만약 rev가 2의 배수이면  -> rev가 원래 배열인 경우(역순의 역순 : 원래 배열)
                    queue.popleft() # queue 맨앞에서 값 제거
                else: # 아닌경우 : 역순인 경우
                    queue.pop() # queue의 맨 뒤에서 값 제거
    
    if flag == 0: # flag가 0 인경우 , 에러가 나지 않은 경우
        if rev%2 == 0: # rev가 해당되지 않는 경우
            print("["+",".join(queue)+"]") # []를 붙이고 ,를 각 숫자에다가 부여해준뒤 출력
        else: # rev가 해당되는 경우
            queue.reverse() # queue를 역순으로 바꿔
            print("["+",".join(queue)+"]") # []를 붙이고 ,를 각 숫자에다가 부여해준뒤 출력
```
- 시간 복잡도 줄이는게 관건
