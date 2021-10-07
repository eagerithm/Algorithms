# 운동 (https://www.acmicpc.net/problem/1956)
# 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 
# 주의. 두 마을을 왕복하는 경우도 사이클에 포함됨

# 나의 정답 - 플로이드 와셜을 통해 모든 정점 간 최단거리 계산 후 두 정점을 오가는 최단거리들 비교
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

INF = 999999*V

distance = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    A, B, d = map(int, input().split()) 
    distance[A][B] = d # (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

for i in range(V+1):
    distance[i][i] = 0

# 플로이드 와셜
for mid in range(1, V+1):
    for start in range(1, V+1):
        for end in range(1, V+1):
            distance[start][end] = min(distance[start][end], distance[start][mid] + distance[mid][end])

min_cycle = INF

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j: continue
        if min_cycle > distance[i][j] + distance[j][i]:
            min_cycle = distance[i][j] + distance[j][i]

print(min_cycle if min_cycle != INF else -1)

# =================================================================
# 시간초과 - 유니온 파인드 활용
import sys
import heapq 

input = sys.stdin.readline

V, E = map(int, input().split())

INF = 999999*V

distance = [[INF]*(V+1) for i in range(V+1)]

edges = []
for _ in range(E):
    A, B, d = map(int, input().split()) 
    heapq.heappush(edges, (d, A, B)) # (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

parent = [i for i in range(V+1)]
def find_ancestor(child):
    if parent[child] != child:
        parent[child] = find_ancestor(parent[child])
    return parent[child]

def unite(A, B):
    pa = find_ancestor(A)
    pb = find_ancestor(B)
    if pa == pb:
        return True # is cycle
    elif pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa
    return False

cycle_parent = -1
cycle_start = -1
cycle_second = -1

while edges:
    d, cur, next = heapq.heappop(edges)
    distance[cur][next] = d # 중복X
    if unite(cur, next):
        cycle_parent = find_ancestor(cur)
        cycle_start = cur
        cycle_second = next
        break

if cycle_parent == -1:
    print(-1)
else:
    (cur, next) = (cycle_start, cycle_second)
    cycle_memebers = []
    for i in range(1, V+1):
        if find_ancestor(i) == cycle_parent:
            cycle_memebers.append(i)
    dist = distance[cur][next]
    while next != cycle_start: # 다시 시작점으로 돌아온 직후에 종료
        cur = next
        for m in cycle_memebers:
            if distance[cur][m] != INF:
                next = m
                dist += distance[cur][next]
                break
    print(dist)

# =================================================================