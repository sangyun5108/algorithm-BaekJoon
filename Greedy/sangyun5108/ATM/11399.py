import sys

n = int(sys.stdin.readline().rstrip())

need_time = list(map(int,sys.stdin.readline().rstrip().split()))
result = 0

need_time.sort()

person_time = 0

for i in need_time:
    person_time += i
    result += person_time

print(result)