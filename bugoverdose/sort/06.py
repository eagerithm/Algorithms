# https://www.acmicpc.net/problem/2108

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다

import sys

input = sys.stdin.readline

length = int(input())
nums = []
nums_count = {}

for i in range(length):
    number = int(input())
    nums.append(number)
    if number not in nums_count.keys():
        nums_count[number] = 0
    nums_count[number] += 1

nums.sort()

max_occur = 9999
max_occur_count = max(nums_count.values())

for k, v in sorted(nums_count.items(), key=lambda x:x[0]):
    if v == max_occur_count:
        if max_occur != 9999:
            max_occur = k
            break
        max_occur = k
    
print(f'{sum(nums)/length:.0f}')
print(nums[(length-1)//2])
print(max_occur)
print(max(nums) - min(nums))

# =========================================
# 5
# 1
# 3
# 8
# -2
# 2

# 2
# 2
# 1
# 10