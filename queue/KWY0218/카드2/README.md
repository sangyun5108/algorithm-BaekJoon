## Sol 2164
1부터 입력받은 정수까지의 수열을 deque로 만든다.

deque의 길이가 1이 될때 까지, popleft() 한번, append(popleft()) 한번을 반복하고, 반복문을 나오면 마지막 요소를 pop 한다.
