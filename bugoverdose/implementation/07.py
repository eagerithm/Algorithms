# Forming a Magic Square (https://www.hackerrank.com/challenges/magic-square-forming/problem)
# 존재 가능한 형식은 애초에 딱히 몇 가지밖에 없음.

matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))

root = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

possibles = [root]

for _ in range(3):
    original = possibles[-1]
    next = [[0]*3 for _ in range(3)]
    dp = [original[2][0], original[1][0]]
    for col in range(3):
        dp.append(original[0][col])
        next[0][col] = dp[-3]
    for row in range(1, 3):
        dp.append(original[row][2])
        next[row][2] = dp[-3]
    for col in range(1, -1, -1):
        dp.append(original[2][col])
        next[2][col] = dp[-3]
    next[1][0] = dp[-2]
    next[1][1] = 5
    possibles.append(next)

for idx in range(4):
    original = possibles[idx]
    reflected_root = [[0]*3 for _ in range(3)]
    for y in range(3):
        for x in range(3):
            reflected_root[y][x] = original[x][y]
    possibles.append(reflected_root)

min_sum = 99999
for possible in possibles:
    cur_sum = 0
    for y in range(3):
        for x in range(3):
            cur_sum += abs(possible[y][x] - matrix[y][x])
    min_sum = min(cur_sum, min_sum)

print(min_sum)

#  =================================================================
# 입력: [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
# 출력: 7

# 5 3 4
# 1 5 8
# 6 4 2

# 8 3 4
# 1 5 9
# 6 7 2