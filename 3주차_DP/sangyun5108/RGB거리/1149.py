import sys

test_case = int(sys.stdin.readline().rstrip())

dp = {}

result = []

for i in range(test_case):
    rgb_list = list(sys.stdin.readline().rstrip().split())
    dp[i] = rgb_list


