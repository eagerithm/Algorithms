# 파도반 수열
# https://www.acmicpc.net/problem/9461

# 나의 정답
import sys

input = sys.stdin.readline

N = int(input())

nums = []
padoban = [0, 1, 1, 1, 2, 2]

for n in range(N):
    nums.append(int(input()))

for n in range(6, max(nums)+1):
    padoban.append(padoban[(n-1)] + padoban[(n-5)])

for num in nums:
    print(padoban[num])

# =================================================================
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9

# P(6) = P(5) + P(1)
# P(7) = P(6) + P(2)
# P(8) = P(7) + P(3)
# P(9) = P(8) + P(4)
# P(10) = P(9) + P(5)

# =================================================================