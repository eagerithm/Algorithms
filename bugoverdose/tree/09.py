# 사이클 게임 (https://www.acmicpc.net/problem/20040)

# 사이클 : 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.
# 주의. 모든 정점/간선이 아니라 특정 정점들에 대해서만이라도 사이클이 성립하는지를 확인

# 나의 정답 : 이미 서로 같은 집합인데 또 연결하면 사이클이 생성됨 - 사이클의 구성요소는 몰라도 되는 상황 - 시점만 필요
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N)]

def get_ancestor(cur):
    if parent[cur] == cur:
        return cur
    return get_ancestor(parent[cur])

counter = 0
is_cycle = False

for _ in range(M):
    A, B = map(int, input().split())

    if is_cycle: continue

    counter += 1
    pa = get_ancestor(A)
    pb = get_ancestor(B)

    if pa == pb: # 이미 같은 집단인데 서로 연결하려는 경우 사이클 최초 생성
        is_cycle = True
        continue

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

if is_cycle:
    print(counter)
else:
    print(0)

# ==================================================================