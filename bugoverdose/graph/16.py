# 타임머신 (https://www.acmicpc.net/problem/11657)

# Bellman-Ford 알고리즘 : 한 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘
# 다익스트라 알고리즘에 비해 느리지만 벨만포드는 가중치가 음수일 때도 사용 가능
# 다만, 음수 가중치가 사이클을 이루는 경우 (정점들 사이를 오갈수록 최단거리가 더 짧아지므로) 사용 불가능

# 방법: 정점의 개수(N)만큼 최단거리 갱신 반복, 나머지 1번째에서도 최단거리가 갱신되면 음의 순환이 발생하고 있다고 간주

# 작동 원리
# 시작 노드에 대해서 거리를 0으로 초기화, 나머지 노드는 거리를 무한으로 설정
# 정점 수(N)만큼 매 반복 마다 모든 간선 확인 + 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
# n-1번 반복 이후, n번째 반복에서도 거리 값이 갱신된다면 음수 순환이 존재 => 중요!!!

# 다익스트라와의 차이점은 매 반복마다 `모든 간선을 확인`한다는 것입니다. 
# 다익스트라는 방문하지 않는 노드 중에서 `최단 거리가 가장 가까운 노드만`을 방문

# 나의 정답 
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
INF = 99999*E

edges = [] # 다익스트라와 달리 매번 모든 간선 정보 필요하므로 배열로 그대로 사용 
for _ in range(E):
    A, B, w = map(int, input().split())
    edges.append((A, B, w))

# 벨만포드
distance = [INF]*(V+1)
distance[1] = 0 # 시작점까지의 거리만 0으로 초기화

is_negative_cycle = False

for count in range(1,V+1): # 총 V-1번 최단거리 갱신. 
    for idx in range(E): 
        cur, next, weight = edges[idx]
        if distance[cur] == INF: continue # 아직 도달 안함. 해당 노드를 거쳐 다음 노드로 이동불가.
        if distance[next] > distance[cur] + weight:
            distance[next] = distance[cur] + weight
            if count == V:
                is_negative_cycle = True # V번째에도 갱신될 수 있다면 사이클 존재!!
                break

if is_negative_cycle:
    print(-1) # (A) 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다.
else:
    for i in range(2, V+1): # (B) 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 
        print(distance[i] if distance[i] != INF else -1) # 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.

# ==================================================================
