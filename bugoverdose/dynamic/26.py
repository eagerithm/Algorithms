# 내리막 길 (https://www.acmicpc.net/problem/1520)
# 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

# 나의 정답 

#  =================================================================
# 오답 - 두 경로가 교차하는 경우 누락 - 덧셈이 아니라 곱셈이 되어야 함
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

counter = [0]

def dfs(cur_y, cur_x):
    if visited[cur_y][cur_x]:
        counter[0] += 1
        return

    visited[cur_y][cur_x] = True

    if cur_y == N-1 and cur_x == M-1:
        counter[0] += 1
        return 

    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if 0 <= next_x < M and 0 <= next_y < N:
            if board[cur_y][cur_x] > board[next_y][next_x]:
                dfs(next_y, next_x)

dfs(0,0)

print(counter[0])

#  =================================================================
# 시간초과 - 단순 DFS
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

count = [0]

def dfs(cur_y, cur_x):
    if cur_y == N-1 and cur_x == M-1:
        count[0] += 1
        return 
    if cur_y > 0:
        if board[cur_y][cur_x] > board[cur_y-1][cur_x]:
            dfs(cur_y-1, cur_x)
    if cur_y < N-1:
        if board[cur_y][cur_x] > board[cur_y+1][cur_x]:
            dfs(cur_y+1, cur_x)
    if cur_x > 0:
        if board[cur_y][cur_x] > board[cur_y][cur_x-1]:
            dfs(cur_y, cur_x-1)
    if cur_x < M-1:
        if board[cur_y][cur_x] > board[cur_y][cur_x+1]:
            dfs(cur_y, cur_x+1)

dfs(0,0)

print(count[0])

# =================================================================