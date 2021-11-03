# https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input()) # 6

cards = deque([i for i in range(1,N+1)])
# deque([1, 2, 3, 4, 5, 6])

while cards:
    if len(cards) == 1:
        break
    cards.popleft() # deque([2, 3, 4, 5, 6])  | [4, 5, 6, 2] | [6, 2, 4] | ... | [4]
    cards.rotate(-1) # deque([3, 4, 5, 6, 2]) | [5, 6, 2, 4] | [2, 4, 6] | ... | [4]

print(cards[0]) # 4

# ======================================
# 큐 - BFS 문제풀이에 활용

from collections import deque

queue = deque()
# queue = deque([1,2,3]) # 1, 2, 3이 든 상태로 시작

queue.append(1) # 오른쪽에 값 추가
queue.append(2)
queue.append(3)
queue.popleft() # 가장 왼쪽의 값 제거

queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
queue.popleft()

print(queue) # deque([3, 4, 5, 6, 7])
queue.reverse()
print(queue) # deque([7, 6, 5, 4, 3])
print(list(queue)) # [7, 6, 5, 4, 3]

# ==============================================
if queue:
    print("deque is not empty")

while(queue):
    print("while deque is not empty, remove one by one")
    queue.popleft()

# ==============================================
