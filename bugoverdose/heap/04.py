# 최대 힙 (https://www.acmicpc.net/problem/11279)
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

import sys
import heapq # 최소 힙 => 모든 값에 -1를 곱해서 넣고, 뺐을 때도 -1를 곱해서 사용하면 최대 힙처럼 사용 가능

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, -n) 
    else:
        max_val = 0
        if len(heap) > 0:
            max_val = heapq.heappop(heap)
        print(-max_val)

# ==================================================================