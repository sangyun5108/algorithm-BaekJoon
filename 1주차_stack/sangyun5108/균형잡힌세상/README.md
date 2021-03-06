# 문제 : 균형잡힌 세상(실버IV)

세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

## 입력
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

## 출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

## 구현 알고리즘

```python
  while True: # 계속 반복
    value = input() # value 값 받아!
    stack = [] # stack 만들어
 
    if value == '.': # value가 '.'이면
        break # 끝내
    
    for i in value: # . 아니면 value 원소 하나하나 뒤져
        if i == '(' or i == '[': # 원소가 '(' 또는 '['이면
            stack.append(i) # stack에 추가해

        elif i == ']': # 원소가 ']'이면
            if len(stack)!=0 and stack[-1] =='[': # stack 길이가 0이 아니고(stack안비어있음) stack 맨 위의 값이 '['이면
                stack.pop() # stack 맨위에 값 빼버려, 왜? [ ]는 한 짝이므로 짝을 맞춰줌
            else: # 길이가 0이거나 stack 맨 위의 값이 '['이 아니면
                stack.append(']') # stack에 추가해 왜? 짝이 안맞음
                break # 짝 못맞춰준
        
        elif i == ')': # 위에 나온 ]랑 똑같은 로직으로 실행
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0: # 최종적으로 짝이 다 맞춰지면 stack 길이 0됨
        print('yes') # yes 출력
    else: # 짝 다 안맞춰짐
        print('no') # no 출력
```
