# 두 수의 합 (https://www.acmicpc.net/problem/3273)
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

N = int(input())
seq = list(map(int, input().split()))
seq.sort()
target = int(input())

answer = 0

left = 0
right = N-1
while left < right:
    cur_sum = seq[left] + seq[right]
    if cur_sum == target:
        answer += 1
        left += 1 # 혹은 right -= 1
    elif cur_sum < target:
        left += 1
    elif cur_sum > target:
        right -= 1

print(answer)

# ==================================================================