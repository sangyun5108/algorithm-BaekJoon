import sys

test_case = int(sys.stdin.readline().rstrip())

dp = {
 1:1,
 2:1,
 3:1,
 4:2,
 5:2,
 6:3,
 7:4,
 8:5,
 9:7,
 10:9
}

def P(n):
    return n

for i in range(test_case):
    num = int(sys.stdin.readline().rstrip())
    if num>=len(dp):
        for i in range(10,num+1):
            dp[i] = dp[i-3]+dp[i-2]
    print(dp[num])