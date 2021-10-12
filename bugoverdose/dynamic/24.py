# 행렬 곱셈 순서 (https://www.acmicpc.net/problem/11049)
# 행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 나의 정답 

import sys

input = sys.stdin.readline

N = int(input())

matrix_set = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix_set.append((r, c))

dp = [[0]*N for _ in range(N)] # ex) dp[2][4] = (BCD) 행렬곱의 최소값(2~4번째)

for gap in range(1, N):
    for y in range(N-gap):
        a, _ = matrix_set[y]
        _, c = matrix_set[y+gap]

        dp[y][y+gap] = 2 ** 31
        for mid in range(y, y+gap): 
            _, b = matrix_set[mid]
            dp[y][y+gap] = min(dp[y][y+gap], dp[y][mid] + dp[mid+1][y+gap] + a*b*c)
            # dp[y][mid] + dp[mid+1][y+gap] : y ~ mid번째 행렬까지 & mid+1 ~ y+gap번째 행렬까지 
            # (A)(BCD) => dp[0][0] + dp[1][3] + a*b*c
            # (AB)(CD) => dp[0][1] + dp[2][3] + a*b*c
            # (ABC)(D) => dp[0][2] + dp[3][3] + a*b*c

print(dp[0][-1])

# =================================================================
# 오답 - 2개씩, 3개씩 인접한 행렬들끼리 묶으며 최소값들을 누적해가는 방식은 틀림
# 반례 : (AB)(CDE)처럼 따로 2개 이상의 묶음들끼리 모이는 경우가 누락됨

import sys

input = sys.stdin.readline

N = int(input())

matrix_set = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix_set.append((r, c))

dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for idx in range(N-i):
        left = idx
        right = idx+i
        r1, c1 = matrix_set[left]
        r2, c2 = matrix_set[right]
        dp[i][idx] = min(r1*c1*c2 + dp[i-1][idx+1], dp[i-1][idx] + r1*r2*c2) # ()( , , ) vs ( , , )()

print(dp[-1][0]) # dp = [[0, 0, 0], [30, 36, 0], [90, 0, 0]]

# =================================================================
