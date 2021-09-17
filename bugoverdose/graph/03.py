# 방의 개수
# 오일러의 다면체 정리(2차원): F = 1 + E - V 
#                     (3차원): F = 2 + E - V  # the number of vertices(꼭지점), minus the number of edges(변), plus the number of faces(면), is equal to two

# 1) 기존에 만들어진적 없는 간선이 새롭게 생성되면서 
# 2) 이전에 지나간 정점을 재방문하는 경우에 새로운 방이 생성된다 
# 3) 다만 X자로 교차하면서 한번에 방이 2개 생성될 가능성도 존재 
# => X자 교체 문제 해결을 위해 2배로 늘리기 => (0.5, 0.5) 같은 정점들을 전부 (1, 1)로 늘리기

# 나의 정답 
def solution(arrows):
    face_count = 0
    direction = [(0, 1), (1, 1), (1, 0), (1, -1),
                 (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    visited_v = {} # 특정 노드 방문 여부
    visited_e = {} # 특정 경로 지나갔는지의 여부
    
    queue = [(0,0)] # 각 노드들 지나간 순서대로 대입
    
    for i in range(len(arrows)):
        next_dir = direction[arrows[i]]
        for _ in range(2):
            queue.append((queue[-1][0] + next_dir[0], queue[-1][1] + next_dir[1]))
            visited_v[queue[-1]] = False
            visited_e[(queue[-2], queue[-1])] = False
    
    cur_node = queue.pop(0)
    visited_v[cur_node] = True
    
    while queue:
        next_node = queue.pop(0)
        
        if visited_v[next_node] == True:
            if visited_e[cur_node, next_node] == False:
                face_count += 1
        else:
            visited_v[next_node] = True
        
        visited_e[cur_node, next_node] = True
        visited_e[next_node, cur_node] = True
        cur_node = next_node
    
    return face_count

# =================================================================
# 다른 사람의 풀이 - 오일러의 다면체 정리(2차원): f = 1+e-v 
def solution(arrows): 
    nodes = set() # {(0,0), (-1,0), ...} # set이므로 동일 데이터 들어오면 새로 추가되지 않음. (중복X)
    edges = set()
    (start_x, start_y)=(0,0)
    direction=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    nodes.add((start_x, start_y))
    
    for a in arrows:
        for i in range(2):
            (next_x, next_y)=(cur_x + direction[a][0], cur_y + direction[a][1])
            nodes.add((next_x, next_y))
            if (cur_x,cur_y)>(next_x, next_y): # tuple 간의 비교는 문자열 간의 비교와 동일 (1,2,3) > (1,2,2)
                edges.add(((cur_x,cur_y), (next_x, next_y))) # 개수가 중요하므로 한 가지 케이스만 일관되게 추가/덮어씌어지도록
            else:
                edges.add(((next_x, next_y), (cur_x,cur_y)))                     
            (cur_x,cur_y) = (next_x, next_y)

    return 1+len(edges)-len(nodes)

# =================================================================