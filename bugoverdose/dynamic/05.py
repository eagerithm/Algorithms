# 피보나치 함수
# https://www.acmicpc.net/problem/1003
# fibonacci(1)은 1을 출력 & fibonacci(0)은 0을 출력

# 나의 정답
import sys

input = sys.stdin.readline

N = int(input()) # N은 40보다 작거나 같은 자연수 또는 0

zero_ones = {}

def fibonacci(n, zero_ones):
    if n == 0:
        zero_ones[0] = [1, 0]
        return zero_ones
    elif n == 1:
        zero_ones[1] = [0, 1]
        return zero_ones
    else:
        z1, o1 = zero_ones[n-2]
        z2, o2 = zero_ones[n-1]
        zero_ones[n] = [z1+z2, o1+o2]
        return zero_ones

for i in range(41):
    zero_ones = fibonacci(i, zero_ones)

for _ in range(N):
    result = int(input())
    print(zero_ones[result][0], zero_ones[result][1])

# =================================================================
# 다른 사람의 풀이
import sys
T = int(input())
dp = [[1,0], [0,1]]
q = [int(sys.stdin.readline()) for _ in range(T)]

for i in range(2,max(q)+1):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
for i in q:
    print(dp[i][0], dp[i][1])
    
# =================================================================
# 메모리 초과
# 단순 재귀로 피보나치 수를 구하면 왜 느릴까요? 함수 호출의 개수가 기하급수적으로 늘어나기 때문입니다.
import sys

input = sys.stdin.readline

N = int(input())

def fibonacci(n):
    if n == 0 or n == 1:
        return [n]
    else:
        return fibonacci(n-2) + fibonacci(n-1)

for _ in range(N):
    result = fibonacci(int(input()))
    print(result.count(0) , result.count(1))

# =================================================================