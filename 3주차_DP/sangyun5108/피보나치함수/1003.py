import sys

zero = [1,0,1]
one = [0,1,1]

def fibonacci(n):
    length = len(zero)
    if n>=length:
        for i in range(length,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[n],one[n]))

test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    fibonacci(int(sys.stdin.readline().rstrip()))

