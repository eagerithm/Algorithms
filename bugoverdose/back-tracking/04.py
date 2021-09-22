# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 M개를 고른 수열
# 중복 포함
# 각 수열 자체가 오름차순

# 나의 정답
N, length = map(int, input().split())
count = 1
nums = [[i] for i in range(1,N+1)]

while count < length:
    prev_nums = nums
    cur_nums = []
    for nums in prev_nums:
        biggest = nums[-1]
        for i in range(biggest, N+1):
            cur_nums.append(nums + [i])
    nums = cur_nums
    count += 1

for num in nums:
    print(' '.join(map(str, num)))

# =================================================================
# 다른 사람의 풀이
from itertools import combinations_with_replacement

n, m = map(int, input().split())

print("\n".join(map(" ".join, combinations_with_replacement(map(str, range(1, n+1)), m))))

# =================================================================
# 3 3 (input)

# 1 1 1 (output)
# 1 1 2
# 1 1 3
# 1 2 2
# 1 2 3
# 1 3 3
# 2 2 2
# 2 2 3
# 2 3 3
# 3 3 3
# =================================================================