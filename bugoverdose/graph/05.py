# 바이러스 (https://www.acmicpc.net/problem/2606)
# 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

import sys
from collections import deque

input = sys.stdin.readline

V = int(input()) # vertex 정점
E = int(input()) # edge 간선

edges = {}

for i in range(V):
    edges[i+1] = deque()

for _ in range(E):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

queue = deque([1])
visited = [1]

while queue:
    cur = queue[0]
    
    for _ in range(len(edges[cur])):
        next = edges[cur].popleft()
        if next not in visited:
            visited.append(next)
            queue.append(next)
    
    queue.popleft()

print(len(visited)-1)

# =================================================================
# 다른 사람의 풀이
import sys

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())

dic = {k:[] for k in range(1,n + 1)}
for _ in range(r):
    
    a,b = map(int,sys.stdin.readline().split())
    dic[a] += [b]
    dic[b] += [a]

visit = [1]
Q = [1]

while Q:
    tmp = Q.pop(0) # 처음에 제거해도 무관함
    nextQ = [x for x in dic[tmp] if x not in visit]
    Q += nextQ
    visit += nextQ
print(len(visit) - 1)

# =================================================================