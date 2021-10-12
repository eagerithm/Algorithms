# 연속합 (https://www.acmicpc.net/problem/1912)
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

cur_sum = nums[0]
max_sum = cur_sum

for cur in nums[1:]:
    if cur_sum + cur >= cur: # 이전 값들에 현재 값을 이어붙이는게 이득인지 확인 
        cur_sum += cur
    else:
        cur_sum = cur # 현재 값 붙였을 때 값 감소할 것 같으면 이전 값들 다 없애고 현재 값부터 다시 시작
    max_sum = max(max_sum, cur_sum) 

print(max_sum)

# =================================================================
