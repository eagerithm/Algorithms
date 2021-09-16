# 가장 먼 노드
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# 입출력 예
# n	    vertex	                                                    return
# 6	    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

# 나의 정답 - 다익스트라 알고리즘 - 특정 노드로부터의 각 노드까지의 최단거리
from heapq import *

def solution(n, edge):
    heap = [(0, 1)] # 노드 1에서의 최단거리: 0
    connected = {}
    final_distances = {}
    
    for i in range(n):
        connected[i+1] = []
        
    for e in edge:
        node_a, node_b = e
        connected[node_a].append(node_b)
        connected[node_b].append(node_a)        
    
    while heap:
        min_dist, cur_node = heappop(heap)
        
        if cur_node not in final_distances.keys():
            final_distances[cur_node] = min_dist
        elif final_distances[cur_node] > min_dist:
            final_distances[cur_node] = min_dist
        else: 
            continue
        
        for next_node in connected[cur_node]:
            
            if next_node in final_distances.keys():
                continue # 이미 순회했으므로 생략. 순환참조 예방.
            heappush(heap, (min_dist+1, next_node))
    
    distances = list(final_distances.values())
    farthest = max(distances)
    
    answer = distances.count(farthest)
    
    return answer

# =================================================================
# 다른 사람의 풀이 
def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer
    
# =================================================================
# 시간초과
from heapq import *

def solution(n, edge):
    heap = [(0, 1)] # 노드 1에서의 최단거리: 0
    final_distances = {}
    
    while heap:
        min_dist, cur_node = heappop(heap)
        
        if cur_node not in final_distances.keys():
            final_distances[cur_node] = min_dist
        elif final_distances[cur_node] > min_dist:
            final_distances[cur_node] = min_dist
        else: 
            continue
        
        i = 0
        while i < len(edge):
            node_a, node_b = edge[i]
            
            if cur_node != node_a and cur_node != node_b:
                i += 1
                continue                     
            
            if cur_node == node_a:
                heappush(heap, (min_dist+1, node_b))            
            else:
                heappush(heap, (min_dist+1, node_a))
            
            edge.pop(i)
    
    distances = list(final_distances.values())
    farthest = max(distances)
    
    return distances.count(farthest)

# =================================================================