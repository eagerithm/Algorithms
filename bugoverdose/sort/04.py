# 시간 복잡도가 O(n²)인 정렬 알고리즘

# 버블 정렬 : 인접된 요소 2개씩 서로 대소비교해가며 자리 바꾸는 작업을 반복
#  1바퀴 돌면 가장 큰 값은 자연스럽게 맨 끝에 위치. 
#  2바퀴 돌면 두번째로 큰 값은 끝에서 두번째에 위치.

import sys

input = sys.stdin.readline
length = int(input())
nums = []

for i in range(length):
    nums.append(int(input()))

for _ in range(length-1):
    for i in range(length-1):
        a, b = nums[i], nums[i+1]
        if a > b:
            nums[i], nums[i+1] = b, a

for i in range(length):
    print(nums[i])

# =========================================
# 선택 정렬 : 처음부터 끝까지 검색하여 매번 가장 작은 값을 선택하는 작업 반복하며, 매번 맨 앞의 위치에 순차적으로 할당.
# 비교대상을 순차적으로 하나씩 제거하므로 성능개선됨
import sys

input = sys.stdin.readline
length = int(input())
nums = []
answer = []

for i in range(length):
    nums.append(int(input()))

while nums:
    min_idx = 0
    for idx in range(len(nums)):
        if nums[idx] < nums[min_idx]:
            min_idx = idx
    answer.append(nums.pop(min_idx))

for i in range(len(answer)):
    print(answer[i])

# =========================================