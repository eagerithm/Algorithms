# 부분합 (https://www.acmicpc.net/problem/1806)
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

N, S = map(int, input().split())
seq = list(map(int, input().split()))

INF = 999999*N
min_len = INF

left = 0 # idx 기준
right = 0
cur_sum = seq[0] # 매번 sum(seq[left:right+1])하면 시간초과
while True:
    if cur_sum < S: # 작으면 범위를 더 넓혀야 함
        right += 1
        if right >= N: break
        cur_sum += seq[right]
    elif S <= cur_sum: # 크거나 같으면 범위를 좁혀도 되는지 확인
        if min_len > right - left + 1:
            min_len = right - left + 1
            if min_len == 1: break
        cur_sum -= seq[left]
        left += 1
    
print(min_len if min_len<INF else 0)

# ==================================================================
# 10 15
# 5 1 3 5 10 7 4 9 2 8

# 2