# 구간 합 구하기 5 (https://www.acmicpc.net/problem/11660)
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 
# 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

total_sums = [[0]*N for _ in range(N)]
for row in range(N):
    for col in range(N):
        total_sums[row][col] += sum(board[row][0:col+1])

    if row == 0: continue

    for col in range(N):
        total_sums[row][col] += total_sums[row-1][col]

for _ in range(M):
    row1, col1, row2, col2 = map(lambda x:x-1, map(int, input().split()))
    total_sum = total_sums[row2][col2]
    if row1 > 0:
        total_sum -= total_sums[row1-1][col2]
    if col1 > 0:
        total_sum -= total_sums[row2][col1-1]
    if row1 > 0 and col1 > 0:
        total_sum += total_sums[row1-1][col1-1]

    print(total_sum)

# =================================================================