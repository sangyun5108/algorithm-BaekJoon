## Sol 1966

N : Test 개수

N, M : N = 배열의 크기, M = index

W : 중요도 요소들, indexW : 요소들의 인덱스 배열

요소들의 최대 값이 맨 앞으로 올 때까지 W, indexW를 append(popleft())를 한다.

최대 값이 맨 앞에 왔으면 count 하나 증가하고, 출력할 값의 인덱스가 M과 일치하는지 확인하고, 일치하면 반복문을 빠져나오고 아니면 W, indexW 를 popleft() 한다.
