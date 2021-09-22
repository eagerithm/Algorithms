# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 M개를 고른 수열
# 중복 포함

# 나의 정답
N, length = map(int, input().split())
count = 1
nums = [[i] for i in range(1, N+1)]

while count < length:
    prev_nums = nums
    new_nums = []
    for num in prev_nums:
        for i in range(1, N+1):
            new_nums.append(num + [i])
    nums = new_nums
    count += 1
    
for num in nums:
    print(' '.join(map(str, num)))

# =================================================================
# 다른 사람의 풀이
import itertools
N,M = map(int,input().split())
list1 = list(map(str,range(1,N+1)))

print("\n".join(list(map(" ".join,itertools.product(list1,repeat=M)))))

# =================================================================
# 4 2 (input)

# 1 1 (output)
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4
# =================================================================