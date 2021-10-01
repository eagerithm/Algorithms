# 트리의 부모 찾기 (https://www.acmicpc.net/problem/11725)
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오

# 나의 정답 - BFS : 재귀깊이와 무관 
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

edge = {}

for i in range(1,N+1):
    edge[i] = []

for _ in range(N-1):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

parents = [-1,-1] + [0]*(N-1) # 2번 노드의 부모노드는 parents[2]

queue = deque([1])

while queue:
    cur = queue.popleft()
    for next in edge[cur]:
        if parents[next] != 0: continue
        queue.append(next)
        parents[next] = cur

for parent_node in parents[2:]:
    print(parent_node)
    
# ==============================================================
# DFS - 재귀깊이로 인해 에러 발생 - 너무 깊으면 또 메모리 초과됨
import sys

sys.setrecursionlimit(10**3)

input = sys.stdin.readline

N = int(input())

edge = {}

for i in range(1,N+1):
    edge[i] = []

for _ in range(N-1):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

parents = [-1,-1] + [0]*(N-1) # 2번 노드의 부모노드는 parents[2]

stack = [1]

def dfs(stack, parents):
    cur = stack.pop()
    for next in edge[cur]:
        if parents[next] != 0: continue
        stack.append(next)
        parents[next] = cur
        stack, parents = dfs(stack, parents)
    return stack, parents

stack, parents = dfs(stack, parents)

for parent_node in parents[2:]:
    print(parent_node)
# ==============================================================
# 입력
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

# 출력
# 4
# 6
# 1
# 3
# 1
# 4

# 이해
#     1
#  6     4
#  3    2 7
#  5