# 평범한 배낭 (https://www.acmicpc.net/problem/12865) 
# N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다. 
# 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
# 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자. 

# 나의 정답 
import sys

input = sys.stdin.readline

N, W = map(int, input().split())

dp = [0]*(W+1) # dp[weight_sum] = max_value_sum

for _ in range(N):
    weight, value = map(int, input().split())
    if weight > W: continue
    if value == 0: continue

    for cur_sum in range(W, weight, -1):
        if dp[cur_sum - weight] == 0: continue
        if dp[cur_sum] < dp[cur_sum - weight] + value:
            dp[cur_sum] = dp[cur_sum - weight] + value

    if dp[weight] < value:
        dp[weight] = value

print(max(dp)) # dp = [0, 0, 0, 6, 8, 12, 13, 14]

# =================================================================
# 시간초과 - meet in the middle
import sys

input = sys.stdin.readline

N, W = map(int, input().split())

a_nums = []
b_nums = []

for _ in range(N//2):
    weight, value = map(int, input().split())
    if value == 0: continue
    a_nums.append((weight, value))

for _ in range(N - N//2):
    weight, value = map(int, input().split())
    if value == 0: continue
    b_nums.append((weight, value))

a_sums = [(0, 0)]
b_sums = [(0, 0)]

for cur_w, cur_v in a_nums:
    for w_sum, v_sum in list(a_sums):
        if w_sum + cur_w <= W:
            a_sums.append((w_sum + cur_w, v_sum + cur_v))

for cur_w, cur_v in b_nums:
    for w_sum, v_sum in list(b_sums):
        if w_sum + cur_w <= W:
            b_sums.append((w_sum + cur_w, v_sum + cur_v))

max_val = 0
a_sums.sort(key=lambda x:x[0])
b_sums.sort(key=lambda x:x[0])

for a_w, a_v in a_sums:
    for b_w, b_v in b_sums:
        if a_w + b_w <= W:
            max_val = max(max_val, a_v + b_v)
        else:
            break

print(max_val)

# =================================================================
