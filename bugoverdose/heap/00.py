# https://www.acmicpc.net/problem/2751
# cf) 단순 정렬 성능만 생각하면 sorted(리스트), 리스트.sort()가 더 효율적 

# 힙 정렬 
import sys
import heapq

input = sys.stdin.readline
length = int(input())
nums = []

for i in range(length):
    heapq.heappush(nums, int(input()))

while nums:
    print(heapq.heappop(nums))

# ======================================================