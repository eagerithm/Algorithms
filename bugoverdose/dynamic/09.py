# RGB거리 (https://www.acmicpc.net/problem/1149)
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# input : 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
# output : 모든 집을 칠하는 비용의 최솟값을 출력

# 나의 정답 - 현재 3가지 색 중 하나를 칠했을 경우, 해당 경우에 도달하기까지의 최소값들
import sys

input = sys.stdin.readline

N = int(input())

dp = {'r':[0], 'g':[0], 'b':[0] } # dp[r][i] : i번째를 빨강색으로 칠할 수 있는 경우들 중 최소 비용

for i in range(1, N+1):
    r, g, b = map(int, input().split())
    dp['r'].append(r + min(dp['g'][i-1], dp['b'][i-1]))
    dp['g'].append(g + min(dp['r'][i-1], dp['b'][i-1]))
    dp['b'].append(b + min(dp['r'][i-1], dp['g'][i-1]))

print(min(dp['r'][N], dp['g'][N], dp['b'][N]))

# =================================================================
# 오답 - 시작점을 기준으로 진행하는 방식 
import sys

input = sys.stdin.readline

N = int(input())

r1, g1, b1 = map(int, input().split())

# [prev_rgb, min_sum] 형식
dp1 = [1, r1] # r로 시작
dp2 = [2, g1] # g로 시작
dp3 = [3, b1] # b로 시작

for rgb in range(N-1):
    r, g, b = map(int, input().split())

    for dp in [dp1, dp2, dp3]:
        if dp[0] == 1:
            dp[0] = 2 if g < b else 3
            dp[1] += min(g, b)
        elif dp[0] == 2:
            dp[0] = 1 if r < b else 3
            dp[1] += min(r, b)
        else:
            dp[0] = 1 if r < g else 2
            dp[1] += min(r, g)

print(min(dp1[1], dp2[1], dp3[1]))

# =================================================================