# 최단경로 (https://www.acmicpc.net/problem/1753)
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 주의: 시작점~해당 위치까지 추정되는 총 거리 기준으로 힙 정렬

# 나의 정답 - 다익스트라
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
inf_distance = 10*V
distance = [inf_distance]*(V+1) # distance[i] : 시작점부터 i까지 도달하는 최단거리 정보

edges = {}
for i in range(1, V+1):
    edges[i] = []

for _ in range(E): 
    A, B, w = map(int, input().split()) # 방향그래프 
    edges[A].append((w, B)) # 일방향. 양쪽으로 오갈 수 없음

queue = [(0, start)]
distance[start] = 0 

while queue: 
    _, cur = heappop(queue) # 최소힙: 가장 가까운 곳부터 순회해야 중복 제거 => visited 불필요
    for w, next in edges[cur]:
        if distance[next] > w + distance[cur]: # 기존 경로보다 현재 위치에서 가는게 더 가까우면 갈 곳으로 지정
            distance[next] = w + distance[cur]
            heappush(queue, (distance[next], next)) # 주의: 시작점~해당 위치까지 추정되는 총 거리 기준으로 힙 정렬

for d in distance[1:]:
    if d == inf_distance:
        print("INF")
    else:
        print(d)

# ==================================================================