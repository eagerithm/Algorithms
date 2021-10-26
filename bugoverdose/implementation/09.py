# Non-Divisible Subset (https://www.hackerrank.com/challenges/non-divisible-subset/problem)

# 나머지들의 중복 개수들을 기준으로 나머지들의 종류 선택 - 중앙을 기준으로 반을 나누고 양쪽 중 하나만 선택
N, div = map(int, input().split())
nums = list(map(lambda x:x%div, map(int, input().split())))

counters = [0]*div
for num in nums:
    counters[num] += 1

max_len = 0

if counters[0] > 0:
    max_len += 1

for left in range(1, div):
    right = div - left

    if left >= right:
        if left == right:
            if counters[left] > 0:
                max_len += 1
        break

    if counters[left] < counters[right]:
        max_len += counters[right]
    else:
        max_len += counters[left]

print(max_len)

#  =================================================================
# 오답 : 앞에서부터 채워나가게 되면 누락되는 케이스 많음
N, div = map(int, input().split())
nums = list(map(lambda x:x%div, map(int, input().split())))

max_len = 0

for start_idx in range(N):
    allowed = [True]*div
    counter = 0
    for cur_idx in range(start_idx, N):
        if allowed[nums[cur_idx]]:
            allowed[(div - nums[cur_idx])%div] = False
            counter += 1
    max_len = max(max_len, counter)

print(max_len)

#  =================================================================