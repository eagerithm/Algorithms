# 가운데를 말해요 (https://www.acmicpc.net/problem/1655)
# 지금까지 말한 수 중에서 중간값을 말해야 한다. 만약, 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

# 나의 정답
import sys 
import heapq 

input = sys.stdin.readline 

N = int(input())

small_heap = [] # max heap - 작은 값들의 최대값이 중앙값
big_heap = [] # min heap

for idx in range(N): 
    prev = small_heap[0]*-1 if idx > 0 else 99999
    cur = int(input())

    if len(small_heap) == len(big_heap):
        if prev > cur:
            heapq.heappush(small_heap, -cur)
        if prev <= cur:
            heapq.heappush(big_heap, cur)
            heapq.heappush(small_heap, -1*heapq.heappop(big_heap)) # small이 더 크도록 좌우 균형 맞추기 
    elif len(small_heap) > len(big_heap):
        if prev <= cur:
            heapq.heappush(big_heap, cur)
        if prev > cur:
            heapq.heappush(big_heap, -1*heapq.heappop(small_heap)) # 더 작은 값을 추가하기 전에 좌우 균형 맞추기 
            heapq.heappush(small_heap, -cur)

    print(small_heap[0]*-1)

# ==================================================================
# 다른 사람의 풀이 - 두 힙의 균형 맞추는 작업 최소화
import sys
import heapq

maxq, minq = [], []
n, *nums = map(int, sys.stdin.read().split())
answer = []

for num in nums:
    if not maxq or num <= -maxq[0]:
        heapq.heappush(maxq, -num)
    else:
        heapq.heappush(minq, num)
    diff = len(maxq) - len(minq)
    if diff == 2:
        heapq.heappush(minq, -heapq.heappop(maxq))
        diff = 0
    elif diff == -2:
        heapq.heappush(maxq, -heapq.heappop(minq))
        diff = 0

    answer.append(str(-maxq[0] if diff >= 0 else minq[0]))

print('\n'.join(answer))

# ==================================================================
