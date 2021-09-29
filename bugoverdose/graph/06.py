# 단지번호붙이기 (https://www.acmicpc.net/problem/2667)
# 이차원배열의 지도에서 서로 연결된 1들의 집합들 개수, 각 집합의 1의 개수들 출력

import sys

input = sys.stdin.readline

N = int(input())

houses = []
visited = [[0]*N for _ in range(N)] 

for i in range(N):
    houses.append(list(map(int, list(input().rstrip()))))

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

def dfs(house_num, stack, houses, visited):
    y, x = stack.pop() # 가장 최근에 추가된 집
    for i in range(4):
        cur_x = x+dx[i]
        cur_y = y+dy[i]
        if 0 <= cur_x < N and 0 <= cur_y < N: # 배열의 경계 넘어가면 생략
            if houses[cur_y][cur_x] == 1 and visited[cur_y][cur_x] == 0:
                visited[cur_y][cur_x] = 1
                house_num += 1
                stack = [(cur_y,cur_x)]
                house_num, stack, houses, visited = dfs(house_num, stack, houses, visited)
    return house_num, stack, houses, visited                
            
stack = []
answers = []

for y in range(N):
    for x in range(N):
        if houses[y][x] == 1 and visited[y][x] == 0: # 아직 방문하지 않은 집인 경우
            visited[y][x] = 1
            house_num = 1
            stack.append((y,x))
            house_num, stack, houses, visited = dfs(house_num, stack, houses, visited)
            answers.append(house_num)

print(len(answers))
for length in sorted(answers):
    print(length)

# =================================================================
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3
# 7
# 8
# 9
# =================================================================