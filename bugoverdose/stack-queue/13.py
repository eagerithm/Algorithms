# AC (https://www.acmicpc.net/problem/5430)
# "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수

# 나의 정답
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    is_reversed = False
    commands = input().rstrip()
    first_idx = 0
    last_idx = int(input())

    num_string = input().rstrip()
    queue = []
    if num_string != "[]":
        queue = list(map(int, num_string[1:-1].split(',')))

    for c in commands:
        if c == "R":
            is_reversed = not is_reversed
            continue
        if is_reversed:
            last_idx -= 1
        else:
            first_idx += 1

    if first_idx <= last_idx:
        if is_reversed:
            print('[' + ','.join(map(str, queue[first_idx:last_idx][::-1])) + ']')
        else:
            print('[' + ','.join(map(str, queue[first_idx:last_idx])) + ']') # [1, 2]는 틀림. [1,2]는 맞음
    else:
        print("error")
    
# ==========================================================
# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []

# [2,1]
# error
# [1,2,3,5,8]
# error