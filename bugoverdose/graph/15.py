# 미확인 도착지 (https://www.acmicpc.net/problem/9370)

# 나의 정답 - start에서 직접 각 target에 도달하는 거리들 vs start->p1/p2를 지나서 target에 도달하는 최단거리들 비교
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def get_min_distances(distances, begin, edges):
    queue = [(0, begin)]
    distances[begin] = 0
    while queue:
        _, cur = heappop(queue)
        for weight, next in edges[cur]:
            if distances[next] > distances[cur] + weight:
                distances[next] = distances[cur] + weight
                heappush(queue, (distances[next], next))
    return distances

for _ in range(int(input())):
    V, E, T = map(int, input().split()) # T는 목적지 후보의 수
    infinite = 99999*E
    start, p1, p2 = map(int, input().split())
    
    edges = {}
    for i in range(1,V+1):
        edges[i] = []
    for _ in range(E):
        A, B, w = map(int, input().split())
        edges[A].append((w,B))
        edges[B].append((w,A))

    targets = [int(input()) for _ in range(T)]

    # 시작지점별 최단거리들
    d_from_start = get_min_distances([infinite]*(V+1), start, edges)
    d_from_p1 = get_min_distances([infinite]*(V+1), p1, edges)
    d_from_p2 = get_min_distances([infinite]*(V+1), p2, edges)

    answers = []
    
    # start->p1->p2->targets vs start->targets    
    for t in targets:
        should_be_faster = d_from_start[p1] + d_from_p1[p2] + d_from_p2[t]
        if should_be_faster <= d_from_start[t]:
            answers.append(t)

    # start->p2->p1->targets vs start->targets
    for t in targets:
        should_be_faster = d_from_start[p2] + d_from_p2[p1] + d_from_p1[t]
        if should_be_faster <= d_from_start[t]:
            answers.append(t)

    print(" ".join(map(str, sorted(answers))))

# ==================================================================