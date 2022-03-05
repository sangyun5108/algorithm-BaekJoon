import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

board = [sys.stdin.readline().rstrip() for _ in range(n)]

W_board = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

B_board = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

def check(i,j):
    w_result = 0
    b_result = 0
    for di in range(8):
        for dj in range(8):
            ni,nj = i+di, j+dj
            if board[ni][nj]!=W_board[di][dj]:
                w_result+=1
            if board[ni][nj]!=B_board[di][dj]:
                b_result+=1
    return min(w_result,b_result)

result = 99999999999999

for i in range(n-7):
    for j in range(m-7):
        result = min(result,check(i,j))

print(result)