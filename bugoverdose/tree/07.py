# 집합의 표현 (https://www.acmicpc.net/problem/1717)
# 일방향적인 트리로 각 집합 표현 가능 

# 유니온 파인드 알고리즘이란?
# 그래프 알고리즘의 일종으로서 상호 배타적 집합, Disjoint-set 이라고도 합니다. 
# 여러 노드가 존재할 때 어떤 두 개의 노드를 같은 집합으로 묶어주고, 
# 다시 어떤 두 노드가 같은 집합에 있는지 확인하는 알고리즘입니다. 그러기 위해 두 가지 연산이 존재합니다.
# Find: 노드 x 가 어느 집합에 포함되어 있는지 찾는 연산
# Union: 노드 x가 포함된 집합과 노드 y가 포함된 집합을 합치는 연산

# {1,2,3}, {4,5}, {6} : 집합 3개
# 1-2-3 | 4-5 | 6 : 트리 3개
# 3 3 3   5 5   6 : 각 노드의 최종적인 부모노드를 집단별로 하나로 통일

# 나의 정답
import sys

input = sys.stdin.readline

case_num = 0

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find_parent(cur):
    if cur == parent[cur]:
        return cur
    return find_parent(parent[cur])

def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a < parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

for _ in range(M):
    op, A, B = map(int, input().split())

    if op == 0: 
        if A == B: continue # 자신과 연결하는 작업은 생략
        union(A, B)
    elif op == 1:
        if find_parent(A) == find_parent(B):
            print("YES")
        else:
            print("NO")
    # print(parent) 
    # [0, 3, 4, 7, 4, 5, 7, 7]

# =================================================================
# 메모리 초과
import sys

input = sys.stdin.readline

case_num = 0
dic = {}

N, M = map(int, input().split())

for i in range(N+1):
    dic[i] = set([i])

for _ in range(M):
    op, A, B = map(int, input().split())

    if op == 0:
        if A == B: continue # 자신과 연결하는 작업은 생략
        connections = dic[A]|dic[B]
        for node in connections:
            dic[node] = connections
    elif op == 1:
        if A in dic[B] or B in dic[A]:
            print("YES")
        else:
            print("NO")
    # print(dic)
    # {0: {0}, 1: {1, 3, 6, 7}, 2: {2, 4}, 3: {1, 3, 6, 7}, 4: {2, 4}, 5: {5}, 6: {1, 3, 6, 7}, 7: {1, 3, 6, 7}}

# =================================================================
