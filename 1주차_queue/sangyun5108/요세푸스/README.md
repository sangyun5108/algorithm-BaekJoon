# 문제 : 요세푸스 문제 0 (실버 IV)
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
예제와 같이 요세푸스 순열을 출력한다.

# 예제 입력1
```python
 7 3
```

# 예제 출력1
```python
  <3,6,2,7,5,1,4>
```

# 구현 알고리즘
```python
import sys

input =  sys.stdin.readline
n,k = map(int,input().split()) # n,k 입력
numbers = [i for i in range(1,n+1)] # 1부터 n까지 수를 가진 numbers list 생성
result = [] # 결과를 담을 list 생성
num = 0 # num 변수 생성

for i in range(n): # n번 반복
    num += k-1 # 반복문이 실행될 때마다, 죽은 사람 다음 사람을 기준으로 k-1번째 있는 사람을 죽인다.
    if num>=len(numbers): # num이 numbers list의 길이보다 큰 경우
        num = num%len(numbers) # num을 nubers의 길이로 나눈 나머지 값으로 넣어준다.
    
    result.append(str(numbers.pop(num)))

print("<",", ".join(result)[:],">",sep='') # join을 사용해서 ', '를 각 수마다 처음부터 끝까지 달아준다.
```

# 풀이 방식
![KakaoTalk_Photo_2022-01-27-13-54-41](https://user-images.githubusercontent.com/69062776/151294422-2fa32dfb-f9b1-4b81-89fe-c6362aaaa10a.jpeg)
