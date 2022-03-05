import sys

n = int(sys.stdin.readline().rstrip())
movie = 666

while n:
    if '666' in str(movie):
        n-=1
        if n == 0:
            break
    movie+=1

print(movie)