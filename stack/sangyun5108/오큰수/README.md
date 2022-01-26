# 문제 : 오큰수(골드IV) 

크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

# 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

# 출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

# 구현 알고리즘
```python
n = int(input()) # 수열의 크기 n 입력 받기
numbers = list(map(int,input().split())) # 수열 원소들 입력 받기
result = [-1]*n # 오큰 수가 없는 경우 -1 출력이므로 우선 모든 경우를 -1로 초기화 -> 나중에 조건 안달아줘도 됨
stack = [] # stack 생성


for i in range(n): # n번 반복
    while stack and numbers[stack[-1]]<numbers[i]: # stack이 비어있지 않고, stack의 맨 위에 숫자가 현재 numbers숫자의 i 번째보다 작으면
        result[stack.pop()] = numbers[i] # stack에서 제거한 값을 인덱스로 가지는 result 배열의 값을 numbers[i]의 값으로 초기화 해준다.
    
    stack.append(i) # 위 조건 만족 안하면 i 값(인덱스) stack에 추가

for i in result: 
    print(i,end=' ') # 최종적으로 결과 출력
```

# 풀이과정
![KakaoTalk_Photo_2022-01-26-16-56-19 002](https://user-images.githubusercontent.com/69062776/151124455-50e777a8-ae6d-4d30-b95b-d2a51038098f.jpeg)
![KakaoTalk_Photo_2022-01-26-16-56-18 001](https://user-images.githubusercontent.com/69062776/151124540-df425525-2517-487c-b9ac-8336e2d01e28.jpeg)

