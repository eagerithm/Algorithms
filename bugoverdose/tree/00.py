# 트리 (https://www.acmicpc.net/problem/4803)

# 트리의 주요 공식
# 방향이 있는 트리일 경우: 간선 == 정점 - 1    # A->B
# 방향이 없는 트리일 경우: 간선/2 == 정점 - 1  # A->B, B->A 중복
# cf) 간선 없이 정점 1개여도 트리 1개

# 나의 정답2
import sys

input = sys.stdin.readline

case_num = 0

while True:
    case_num += 1
    V, E = map(int, input().split())

    if V==0 and E==0: break

    edge = {}
    for v in range(1,V+1):
        edge[v] = []

    for _ in range(E):
        A, B = map(int, input().split())
        edge[A].append(B)
        edge[B].append(A)

    tree_num = 0
    visited = [False]*(V+1)
    
    def bfs(node, visited):
        vectors = []
        edges = []
        queue = [node]
        while queue:
            cur = queue.pop()            
            vectors.append(cur)
            visited[cur] = True

            for next in edge[cur]:
                vectors.append(next)
                edges.append((cur, next))
                queue.append(next)
            edge[cur] = []
                
        return vectors, edges, visited

    for cur in range(1,V+1):
        if visited[cur]: 
            continue
        vectors, edges, visited = bfs(cur, visited)
        if len(set(vectors)) == len(edges)//2 + 1:
            tree_num += 1
    
    if tree_num >= 2:
        print(f'Case {case_num}: A forest of {tree_num} trees.')
    elif tree_num == 1:
        print(f'Case {case_num}: There is one tree.')
    else:
        print(f'Case {case_num}: No trees.')

# ===========================================================
# 나의 정답1 
import sys

input = sys.stdin.readline

case_num = 0

while True:
    case_num += 1
    V, E = map(int, input().split())

    if V==0 and E==0: break

    edge = {}
    for v in range(1,V+1):
        edge[v] = []

    for _ in range(E):
        A, B = map(int, input().split())
        edge[A].append(B)
        edge[B].append(A)

    tree_num = 0
    visited = [False]*(V+1)
    
    def bfs(node, visited):
        is_tree = True
        queue = [node]
        while queue:
            cur = queue.pop()
            if visited[cur] == True: # 이미 지나온 노드에 또 도달했다면 사이클 존재 
                is_tree = False # 사이클 발견되어도 break하지 말고 끝까지 다 visit하고 통째로 제거

            visited[cur] = True
            for next in edge[cur]:
                if visited[next] == False:
                    queue.append(next)
        return is_tree, visited

    for cur in range(1,V+1):
        if visited[cur]: 
            continue
        is_tree, visited = bfs(cur, visited)
        if is_tree:
            tree_num += 1
    
    if tree_num >= 2:
        print(f'Case {case_num}: A forest of {tree_num} trees.')
    elif tree_num == 1:
        print(f'Case {case_num}: There is one tree.')
    else:
        print(f'Case {case_num}: No trees.')

# ===========================================================