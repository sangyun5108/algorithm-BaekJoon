import sys

n = int(sys.stdin.readline().rstrip())

meeting_time = []

for i in range(n):
    start_time,end_time = map(int,sys.stdin.readline().rstrip().split())
    meeting_time.append((start_time,end_time))

meeting_time = sorted(meeting_time,key=lambda x:(x[1],x[0]))

before_end_time = 0
cnt = 0

for time in meeting_time:
    start_time = time[0]
    end_time = time[1]

    if start_time >= before_end_time:
        cnt+=1
        before_end_time = end_time

print(cnt)