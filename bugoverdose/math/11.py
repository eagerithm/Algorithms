# 약수 (https://www.acmicpc.net/problem/1037)
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

# 나의 정답
N = int(input())

answer = 1
factors = [] 
nums = sorted(list(map(int, input().split())))

for num in nums:
    cur = num
    for f in factors:
        if cur%f == 0:
            cur = cur//f
        if cur == 1: break 
    if cur > 1:
        factors.append(cur)

for f in factors:
    answer *= f

if answer in nums: 
    answer = answer * nums[0]

print(answer)

# =================================================================
# 2
# 4 2
# 8

# 4
# 2 4 8 16
# 32

# 7
# 2 3 4 6 8 12 16
# 48
# =================================================================