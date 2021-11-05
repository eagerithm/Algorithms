# 섬 연결하기
# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

# 제한사항
# 섬의 개수 n은 1 이상 100 이하입니다.
# costs의 길이는 ((n-1) * n) / 2이하입니다.
# 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
# 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
# 연결할 수 없는 섬은 주어지지 않습니다.

# 입출력 예
# n	    costs	                                        return
# 4	    [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	    4

# 나의 정답 : 유니온 파인드
def solution(n, costs):
    cost = []
    for c in costs:
        cost.append((c[2], c[0], c[1]))
    
    cost.sort(key=lambda x:x[0])
    
    parent = [i for i in range(n)]
    
    def find_parent(child):
        if parent[child] != child:
            parent[child] = find_parent(parent[child])
        return parent[child]
    
    cost_sum = 0
    for c in cost:
        island1, island2 = c[1], c[2]
        
        p1 = find_parent(island1)
        p2 = find_parent(island2)
        
        if p1 == p2: continue
        parent[max(p1, p2)] = min(p1, p2)
        cost_sum += c[0]
    
    return cost_sum

# =================================================================
# 나의 정답
def solution(n, costs):
    total_cost = 0
    costs.sort(key=lambda x:x[2]) # 최소비용부터 정렬
    connections = [{i} for i in range(0, n)] # 연결되지 않은 각 노드별 집합

    for cost in costs: # 최소비용부터 순차적으로 연결
        node_a, node_b, construction_cost = cost
        cur_a_set = set()
        cur_b_set = set() # 연결하려는 두 노드가 현재 각각 어떤 집합에 포함되어있는가
        
        for connected_nodes in connections:
            if node_a in connected_nodes:
                cur_a_set = connected_nodes
            if node_b in connected_nodes:
                cur_b_set = connected_nodes
                
        if cur_a_set == cur_b_set: # 이미 두 노드가 동일한 집합에 포함
            continue # 이미 더 적은 비용으로 연결되었을 것이라 간주

        connections.remove(cur_a_set)
        connections.remove(cur_b_set)
        # connections.append(cur_a_set|cur_b_set)
        connections.append(cur_a_set.union(cur_b_set))
        total_cost += construction_cost
    
    return total_cost

# =================================================================
# 다른 사람의 풀이
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    connect = []
    for i in range(n):
        connect.append({i})
    for i in costs:
        temp0 = set()
        temp1 = set()
        for j in connect:
            if i[0] in j:
                temp0 = j
            if i[1] in j:
                temp1 = j
        if temp0 == temp1:
            continue
        else:
            connect.remove(temp0)
            connect.remove(temp1)
            connect.append(temp0|temp1)
            answer += i[2]
            if len(connect)==1 and len(connect[0])==n-1:
                break

    return answer

# =================================================================