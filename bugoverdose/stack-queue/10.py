# 프린터 큐 (https://www.acmicpc.net/problem/1966)
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 나의 정답 - 큐에서 값을 넣었다 빼는 방식
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())    
    queue = deque()
    nums = list(map(int, input().split()))
    target = nums[M]
    count = 0
    not_found = True
    for idx in range(N):
        queue.append((idx, nums[idx]))

    while not_found:
        max_num = max(list(map(lambda x:x[1], queue)))
        for _ in range(len(queue)):
            cur = queue.popleft()

            if max_num == cur[1]:
                count += 1
                if M == cur[0]:
                    not_found = False
                break
            else:
                queue.append(cur)
    print(count)
    
# ==========================================================