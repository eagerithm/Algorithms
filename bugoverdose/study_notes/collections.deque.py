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
