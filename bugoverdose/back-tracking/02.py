# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 나의 정답
from itertools import combinations

N, length = map(int, input().split())

nums = [i for i in range(1, N+1)]

for c in list(combinations(nums, length)):
    print(' '.join(map(str, c)))

# =================================================================
# 4 2 (input)

# 1 2 (output)
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# =================================================================
# 4 4     (input)

# 1 2 3 4 (output)
# =================================================================