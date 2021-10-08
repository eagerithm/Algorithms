# 1로 만들기 2 (https://www.acmicpc.net/problem/12852)
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2) X가 2로 나누어 떨어지면, 2로 나눈다.
# 3) 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 나의 정답 - 직전 부모 정보를 담은 parent 배열 활용
from collections import deque

N = int(input())

parent = [i for i in range(0, N+1)]

queue = deque([(N, 0)])

while True:
    cur, idx = queue.popleft()
    if cur == 1:
        print(idx)
        break

    idx += 1

    if cur%3 == 0:        
        if parent[cur//3] == cur//3: # 더 낮은 idx에서 이미 조회된 경우 제거
            queue.append((cur//3, idx))
            parent[cur//3] = cur 
    if cur%2 == 0:        
        if parent[cur//2] == cur//2: 
            queue.append((cur//2, idx))
            parent[cur//2] = cur
    if parent[cur-1] == cur-1: 
        queue.append((cur-1, idx))
        parent[cur-1] = cur

cur = 1
answers = [1]
while cur != N:
    cur = parent[cur]
    answers.append(cur)

print(" ".join(map(str, sorted(answers, reverse=True))))

# =================================================================