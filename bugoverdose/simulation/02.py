# 쉽게 푸는 문제 (https://www.acmicpc.net/problem/1292)

A, B = map(int, input().split())

nums = []
for i in range(1,46):
    nums += [i]*i

print(sum(nums[A-1:B]))

# =================================================================