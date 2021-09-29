# 이분 그래프 (https://www.acmicpc.net/problem/1707)
# 그래프 이론에서, 이분 그래프(二分graph, 영어: bipartite graph)란 모든 꼭짓점을 빨강과 파랑으로 색칠하되, 모든 변이 빨강과 파랑 꼭짓점을 포함하도록 색칠할 수 있는 그래프이다.
# In the mathematical field of graph theory, a bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V. Vertex sets U and V are usually called the parts of the graph.

# 나의 정답
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())): # 각 테스트케이스별로 실행
    V, E = map(int, input().split())

    edges = {}
    for i in range(1,V+1):
        edges[i] = deque()

    for _ in range(E):
        A, B = map(int, input().split())
        edges[A].append(B)
        edges[B].append(A)

    visited = [0]*(V+1) # 0이면 unvisited, visit했으면 1과 -1로 구분
    
    answer = "YES"

    for i in range(1,V+1):
        if visited[i] == 0: # 서로 연결되지 않은 첫 정점
            visited[i] = 1
            queue = deque([(i,1)]) # i번 정점을 1번 그룹에
        while queue:
            cur, group = queue.popleft()
            while edges[cur]:
                next = edges[cur].popleft()
                if visited[next] == 0:
                    queue.append((next, group*-1)) # 아직 안지났으면 반대쪽 그룹에 넣기
                    visited[next] = group*-1
                elif visited[next] == group: # 이미 지났고 서로 같은 집단이면 이분 그래프가 아닌 것으로 간주됨
                    answer = "NO"
                    break
            if answer == "NO": break
    if 0 in visited[1:]: # unvisited가 존재하는 경우
        answer = "NO"
    print(answer)

# =================================================================
