# https://www.acmicpc.net/problem/10989

# 계수정렬(Counting Sort) : 중복되는 값들의 개수를 계산하여 순차적으로 출력 
# 메모리 측면에서 우수. 좁은 범위의 숫자들에 대해서는 성능 우월함.

import sys

input = sys.stdin.readline

length = int(input())
nums = [0] * 10001

for _ in range(length):
    num = int(input())
    nums[num] += 1

for num in range(1, 10001):
    if nums[num] != 0:
        for _ in range(nums[num]):
            sys.stdout.write(str(num) + "\n")

# =========================================