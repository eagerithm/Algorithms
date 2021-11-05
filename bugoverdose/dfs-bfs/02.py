# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.
# 입출력 예
# n	computers	return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

# 나의 정답2 - BFS
def solution(n, computers):
    length = len(computers)
    visited = [False]*length
    
    networks = 0
    
    for start_node in range(length):
        if not visited[start_node]:
            networks += 1
            queue = [start_node]
            while queue:
                cur = queue.pop(0)
                visited[cur] = True
                for next_node in range(length):
                    if computers[cur][next_node] != 1: continue
                    if not visited[next_node]:
                        queue.append(next_node)
    return networks

# =================================================================
# 나의 정답 - DFS
def solution(n, computers):
    length = len(computers)
    visited = [False]*length
    
    def dfs(cur_node):
        if visited[cur_node]: return
        visited[cur_node] = True
        neighbors = computers[cur_node]

        for next_node in range(length):
            if neighbors[next_node] == 0: continue
            if visited[next_node]: continue
            dfs(next_node)
        
    networks = 0
    for start_node in range(length):
        if not visited[start_node]:
            networks += 1
            dfs(start_node)
            
    return networks

# =================================================================
# 다른 사람의 풀이 
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

# =================================================================
