# 두 수의 합 (https://www.acmicpc.net/problem/3273)
# 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

N = int(input())
seq = list(map(int, input().split()))
seq.sort()

INF = 9999999999
min_sum = (INF, INF, INF) # (seq[left], seq[right], sum)

left = 0
right = N-1
while left < right:
    cur_sum = seq[left] + seq[right]

    if abs(cur_sum) < abs(min_sum[2]):
        min_sum = (seq[left], seq[right], cur_sum)        
        if cur_sum == 0: break
    
    if cur_sum < 0: # 0보다 작으면 값을 높여야 0에 근접
        left += 1
    elif 0 < cur_sum: # 0보다 크면 값을 낮춰야 0에 근접
        right -= 1
    
print(min_sum[0], min_sum[1])

# ==================================================================
# 5
# -2 4 -99 -1 98

# -99 98