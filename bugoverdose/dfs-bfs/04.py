# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# 입출력 예
# tickets	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# 예제 #1
# ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

# 예제 #2
# ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

# 나의 정답 - DFS
def solution(tickets):
    answer = []
    
    def dfs(start, ticket_list, route):
        route.append(start) 

        if len(ticket_list) == 0:
            answer.append(route)
            return
        
        for ticket in ticket_list:
            if ticket[0] == start:
                tickets_left = ticket_list.copy()
                tickets_left.remove(ticket)
                dfs(ticket[1], tickets_left, route.copy())
                
    dfs("ICN", tickets, [])
    
    return min(answer)

# =================================================================
# 다른 사람의 풀이 
def solution(tickets):
    answer = []

    def dfs(start, ticList, path):
        path.append(start)
        if len(ticList)==1:
            path.append(ticList[0][1])
            answer.append(path)
            return
            
        for t in ticList:
            if t[0]==start:
                ticList_copy = ticList.copy()
                ticList_copy.remove(t)
                dfs(t[1], ticList_copy, path.copy())

    dfs("ICN", tickets, [])
    return min(answer)

# =================================================================
# 다른 사람의 풀이 
from collections import defaultdict

def solution(tickets):
    r = defaultdict(list) # 디폴트값이 list인 dictionary - 값 지정안하면 []로 초기화
    
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []

    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())

    return p[::-1]

# =================================================================
# 다른 사람의 풀이 
def solution(tickets):

    def helper(tickets, route):
        if tickets == []:
            return route
        left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
        if left == []:
            return None
        left.sort(key = lambda i: tickets[i][1])

        for next in left:
            rest = helper(tickets[:next]+tickets[next+1:], route+[tickets[next][1]])
            if rest is not None:
                return rest

    return helper(tickets, ["ICN"])

# =================================================================
# 다른 사람의 풀이 
candidates = []

def visit(start, graph, visited, cnt, route):
    global candidates
    if cnt == len(graph):
        candidates.append(route.split(" "))
    else:
        for i in range(len(graph)):
            if visited[i] == 0 and graph[i][0] == start:
                go = []
                for j in range(len(visited)):
                    go.append(visited[j])
                go[i] = 1
                visit(graph[i][1], graph, go, cnt+1, route+" "+graph[i][1])

def solution(tickets):
    answer = []
    tickets.sort()
    visited = [0] * len(tickets)
    visit("ICN", tickets, visited, 0, "ICN")
    return candidates[0]

# =================================================================