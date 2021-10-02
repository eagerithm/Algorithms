# 여행 가자 (https://www.acmicpc.net/problem/1976)
# 한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다. 동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자. 물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고, 동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행경로를 통해 목적을 달성할 수 있다.
# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오. 같은 도시를 여러 번 방문하는 것도 가능하다.

# 나의 정답 - 유니온 파인드
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)] # 1->2->3인 경우 parent[1] == 3 : 1번의 최상위 부모노드는 3번

def find_parent(child):
    if parent[child] == child:
        return child
    return find_parent(parent[child])

# 직계 부모노드
for cur in range(1,N+1):
    connections = [0] + list(map(int, input().split()))
    for next in range(1,N+1):
        if connections[next] == 1:
            a = find_parent(next)
            b = find_parent(cur)
            if a > b:
                parent[b] = a
            else:
                parent[a] = b
# print(parent) # [0, 2, 3, 3]

# 최상위 부모노드
for cur in range(1,N+1):
    if parent[cur] == cur: continue
    parent[cur] = find_parent(cur)
# print(parent) # [0, 3, 3, 3]

plan = list(set(map(int, input().split())))

common_ancestor = parent[plan[0]]

can_go = True

for p in plan:
    if parent[p] != common_ancestor:
        can_go = False
        break

print("YES" if can_go else "NO")

# =================================================================
# 나의 정답 - BFS
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

edges= {} # ex) edges[3] : 3번에 직접 연결된 모든 곳들
for i in range(1,N+1):
    edges[i] = []

for i in range(1,N+1):
    connections = list(map(int, input().split()))
    for idx in range(N):
        if connections[idx] == 1:
            edges[i].append(idx+1)
    
visited = [0]*(N+1) 
plan = list(set(map(int, input().split())))

start = plan[0]
visited[start] = 1

stack = [start]
while stack:
    cur = stack.pop()
    for next in edges[cur]:
        if visited[next] == 0:
            stack.append(next)
            visited[next] = 1

can_go = True

for p in plan:
    if visited[p] == 0:
        can_go = False
        break

print("YES" if can_go else "NO")

# print(edges, visited, plan)
# {1: [2], 2: [1, 3], 3: [2]} [0, 1, 1, 1] [1, 2, 3]
# =================================================================
