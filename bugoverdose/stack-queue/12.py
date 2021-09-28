# 회전하는 큐 (https://www.acmicpc.net/problem/1021)
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

# 나의 정답
from collections import deque

N, M = map(int, input().split())

targets = list(map(int, input().split()))

queue = deque([i+1 for i in range(N)])

answer = 0

while targets:
    if queue[0] == targets[0]:
        queue.popleft()
        targets.pop(0)
        continue
    if int(len(queue)//2) < queue.index(targets[0]):
        queue.appendleft(queue.pop())
    else:
        queue.append(queue.popleft())
    answer += 1

print(answer)

# =================================================================
# 다른 사람의 풀이 - 최단거리를 누적합 + 새로운 배열을 한번씩 재생성
n, m = map(int, input().split())
dq = [i for i in range(1, n+1)]

ans = 0

for find in map(int, input().split()):
    ix = dq.index(find)
    ans += min(len(dq[ix:]), len(dq[:ix]))
    dq = dq[ix+1:] + dq[:ix]

print(ans)
    
# ==========================================================