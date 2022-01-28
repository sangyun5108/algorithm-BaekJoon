## Sol 9012
입력받은 문자열을 리스트로 바꾼 후, 빈 리스트를 하나 만들고 "(" 이 나오면 리스트에 append, ")"이 나오면 리스트 요소 하나는 pop 한다.
이 때 빈 리스트일 때 ")" 가 나오는 경우를 생각해서 pop을 하기 전에 빈 리스트인지 검사를 한다.

### sys.stdin.readline().strip()
컴파일 속도를 더 빠르게 하기위해서 sys.stdin.readline()을 사용하지만
sys.stdin.readline() 으로 문자열을 입력받고 리스트로 만들면 ['a','b','c','\n'] 이렇게 만들어진다.
줄바꿈을 없애기 위해서 sys.stdin.readline().strip()을 해서 줄바꿈 문자를 없앤다.
