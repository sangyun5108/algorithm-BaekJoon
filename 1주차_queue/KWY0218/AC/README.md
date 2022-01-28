##Sol 5430

reverse 하는 값이 커서 'R' 연산이 나오면 변수 하나를 True False로 토글 시킨다.

True 일 땐 popleft(), False일 땐 pop()을 한다.

연산이 끝난 후 reverse 값이 True일 땐 그대로 출력하고, False이면 리스트를 한번 반전한 후 출력한다.

order의 크기가 N 보다 커도 바로 error를 보내면 안되는 이유는 'RRRRR' 이런식으로 pop 연산을 안 할 수도 있기 때문이다.
