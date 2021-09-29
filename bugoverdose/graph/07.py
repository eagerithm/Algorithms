# 유기농 배추 (https://www.acmicpc.net/problem/1012)
# 이차원배열의 지도에서 서로 연결된 1들의 집합들 개수 출력

# 나의 정답 - BFS
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

for _ in range(int(input())):
    X, Y, N = map(int, input().split())

    groups = 0
    land = [[0]*X for _ in range(Y)]
    visited = [[0]*X for _ in range(Y)]

    for _ in range(N):
        x, y = map(int, input().split())
        land[y][x] = 1

    for y in range(Y):
        for x in range(X):
            if land[y][x] == 1 and visited[y][x] == 0: 
                groups += 1
                visited[y][x] = 1
                queue = deque([(x,y)])
                while queue:
                    xi, yi = queue.popleft()
                    for i in range(4):
                        cur_x = xi+dx[i]
                        cur_y = yi+dy[i]
                        if 0 <= cur_x < X and 0 <= cur_y < Y:
                            if land[cur_y][cur_x] == 1 and visited[cur_y][cur_x] == 0: 
                                visited[cur_y][cur_x] = 1
                                queue.append((cur_x, cur_y))
    print(groups)

# =================================================================
# 메모리 초과 - DFS 사용하면 재귀깊이가 너무 깊어짐
import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

def dfs(land, visited, stack, X, Y):
    x, y = stack.pop()
    for i in range(4):
        cur_x = x+dx[i]
        cur_y = y+dy[i]
        if 0 <= cur_x < X and 0 <= cur_y < Y:
            if land[cur_y][cur_x] == 1 and visited[cur_y][cur_x] == 0: 
                visited[cur_y][cur_x] = 1
                stack.append((cur_x, cur_y))
                land, visited, stack = dfs(land, visited, stack, X, Y)
    return land, visited, stack

for _ in range(int(input())):
    X, Y, N = map(int, input().split())

    groups = 0
    land = [[0]*X for _ in range(Y)]
    visited = [[0]*X for _ in range(Y)]

    for _ in range(N):
        x, y = map(int, input().split())
        land[y][x] = 1

    for y in range(Y):
        for x in range(X):
            if land[y][x] == 1 and visited[y][x] == 0: 
                groups += 1
                visited[y][x] = 1
                stack = [(x,y)]
                land, visited, stack = dfs(land, visited, stack, X, Y)

    stack = None
    land = None
    visited = None
    print(groups)

# =================================================================
# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# 5
# 1
# =================================================================