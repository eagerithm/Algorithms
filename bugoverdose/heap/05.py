# 절댓값 힙 (https://www.acmicpc.net/problem/11286)
# 본질적으로 최소 힙과 동일 - 절대값들에 대해 최소 힙을 적용하면서 tuple로 본래 값도 함께 같은 위치에 저장
# 절대값이 가장 큰 값을 빼내고 싶은 경우, 절대값들 * -1에 대해 최소힙을 적용

# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

import sys
import heapq 

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, (abs(n), n)) 
    else:
        print(heapq.heappop(heap)[1] if len(heap) > 0 else 0)

# ==================================================================