from collections import deque

queue = deque([1,2,3,4,5,6,7,8,9,10])

queue.rotate(1) # 시계방향으로 1칸씩
print(queue)
# deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])

queue.rotate(2) # 시계방향으로 2칸씩
print(queue)
# deque([8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

queue.rotate(-1) # 반시계방향으로 1칸씩
print(queue)
# deque([9, 10, 1, 2, 3, 4, 5, 6, 7, 8])

# ==============================================
# 반시계방향으로 1칸씩
queue.append(queue.popleft())
print(queue)
# deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 시계방향으로 1칸씩
queue.appendleft(queue.pop())
print(queue)
# deque([9, 10, 1, 2, 3, 4, 5, 6, 7, 8])

# ==============================================
