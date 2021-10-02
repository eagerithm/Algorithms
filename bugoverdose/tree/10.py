# 친구 네트워크 (https://www.acmicpc.net/problem/4195)
# 유니온 파인드에 집합의 크기를 구하는 기능을 넣는 문제

# 자신과 자식노드들의 개수를 별도의 dictionary에 저장
# 직속 부모노드 대신 최상위 노드 정보를 parent dictionary에 직접 저장하여 관리

# 나의 정답 
import sys

input = sys.stdin.readline
print = sys.stdout.write

def find_ancestor(cur):
    if parent[cur] == cur:
        return cur
    ancestor = find_ancestor(parent[cur])
    parent[cur] = ancestor # 이미 계산한 값은 다시하지 않아도 되도록 갱신 
    return parent[cur]
    # return find_ancestor(parent[cur]) # 매번 같은 과정 반복하면 시간초과!!!

def merge(A, B): # 두 개의 최상위 부모 노드를 합치면서, 새로운 최상위 노드에 개수 누적 합치기
    pa = find_ancestor(A)
    pb = find_ancestor(B)

    if pa == pb: return
    parent[pb] = pa # pa를 공통된 최상위 부모노드로 삼기
    vector_count[pa] += vector_count[pb] # 같은 집단의 노드 개수를 전부 최상위 노드에 몰빵
    return 

for _ in range(int(input())):
    parent = {}
    vector_count = {} # 자신과 자식노드들의 전체 개수
    for _ in range(int(input())):
        A, B = input().split()

        if parent.get(A) == None: # if A not in parent.keys():
            parent[A] = A
            vector_count[A] = 1
        if parent.get(B) == None:
            parent[B] = B
            vector_count[B] = 1
        
        merge(A, B) # 다른 집단이면 A의 최상위노드에 B의 최상위노드 합치기
        print(str(vector_count[find_ancestor(A)])+"\n")

# ==================================================================