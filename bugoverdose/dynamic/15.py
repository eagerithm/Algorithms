# 동전 1 (https://www.acmicpc.net/problem/2293)
# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

# 나의 정답 - 동전의 종류를 하나씩 늘려가며 각 값을 만들 수 있는 경우의 수를 재계산 
import sys 

input = sys.stdin.readline 

n, k = map(int, input().split()) 

dp = [1] + [0]*(k) # dp[i] = i라는 값을 만들 수 있는 각 경우의 수 (0 <= i <= k)

for _ in range(n):
    coin = int(input()) # 새로운 동전 종류 coin원
    if coin > k: continue 
    for idx in range(coin, k+1):
        dp[idx] += dp[idx-coin] # 기존 경우의 수 + coin원 이전 단계에서 coin을 1개 추가한 경우 = 새로운 경우의 수

print(dp[-1])

# ==================================================================
# 오답 - 구성이 같아도 순서가 다른 경우를 각각 별개로 계산하는 경우
import sys 

input = sys.stdin.readline 

n, k = map(int, input().split()) 

coins = [int(input()) for _ in range(n)] 
coins.sort() 

dp = [0] * (max(coins)-1) + [1] # [0, 0, 0, 0, 1]

for _ in range(k):
    next_num = 0
    for c in coins:
        next_num += dp[-c]
    dp.append(next_num)

print(dp[-1])

# ==================================================================
# 3 10
# 1
# 2
# 5

# 10 

# 1 * 10
# 1 * 8 + 2
# 1 * 6 + 2 * 2
# 1 * 4 + 2 * 3
# 1 * 2 + 2 * 4
# 2 * 5
# 5 * 2
# 1 * 5 + 5 * 1
# 1 * 3 + 2 * 1 + 5 * 1
# 1 * 1 + 2 * 2 + 5 * 1
# ==================================================================