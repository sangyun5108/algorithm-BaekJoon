# 문제 : 스택 수열(실버III)
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

# 입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

# 출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

# 구현 알고리즘
```python
n = int(input()) # 수열을 이루는 수 입력

stack = [] # 스택 생성
answer = [] # 정답 생성
current = 1 # 현재 값
right = 0 # 정답 출력시 필요한 조건

for i in range(n): # n번 반복
    num = int(input()) # 숫자 입력
 
    while (current<=num): # current값이 num보다 작거나 같다면
        stack.append(current) # stack에 current 추가
        answer.append('+') # answer에 + 추가
        current+=1 # curren에 +1
    
    if stack[-1] == num: # stack의 최상단 값과 num이 같은경우
        stack.pop() # stack에서 최상단(맨오른쪽) 값 제거
        answer.append('-') # answer에 - 추가
    else: # stack의 최상단 값과 num이 같지 않은 경우
        print('NO') # No 출력
        right = 1 # right = 1 초기화 -> 정답을 출력해줄 필요가 없어진다.
        break # 반복문 나오기

if right == 0: # 0 인경우
    for i in answer: # answer에 있는 원소 출력
        print(i)
```
# 풀이 과정

![KakaoTalk_Photo_2022-01-26-17-27-33](https://user-images.githubusercontent.com/69062776/151128574-1105adfa-49ea-4336-8e93-870ea9e9b857.jpeg)
