## Sol 1874
몇개의 정수를 입력받을 것인지 입력받고, 만족해야되는 값을 리스트로 받는다.

조건을 확인하면서 1부터 입력받은 값까지의 inteager를 stack에 append 한다.

1. stack의 맨 뒤 요소가 목표 리스트의 현재 index의 값과 같다면 정답 리스트에 "-"를 append 하고 stack을 pop 하고, index 값을 증가한ㄷ.

2. 만약 같지 않다면 stack에 현재 inteager를 append 하고, 정답 리스트에 "+" 를 append 하고 inteager 값을 증가한다.

3. inteager가 입력받은 값까지 stack에 append 했는데, index 값이 입력 받은 값 보다 작으면 index를 증가하면서 1번의 연산을 반복한다.

4. 3번의 연산을 마치고, stack의 값이 비었으면 정답 리스트를 출력하고, 값이 있다면 "NO" 를 출력한다.
