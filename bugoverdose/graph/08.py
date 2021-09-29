# 미로 탐색 (https://www.acmicpc.net/problem/2178)

# BFS의 특징: 각 정점을 최단경로로 방문

# 나의 정답
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

Y, X = map(int, input().split())

maze = [[0]*(X+1)]
visited = [[0]*(X+1) for _ in range(Y+1)]

for _ in range(Y):
    row = list(map(int, list(input().strip())))
    maze.append([0]+row)

counter = 0 # 여태까지 지나온 칸의 개수
queue = deque([(1,1, counter)])
visited[1][1] = 1

while queue:
    x, y, counter = queue.popleft()
    counter += 1 
    if x==X and y==Y: break

    for i in range(4):
        cur_x = x+dx[i]
        cur_y = y+dy[i]
        if 1 <= cur_x <= X and 1 <= cur_y <= Y:
            if maze[cur_y][cur_x] == 1 and visited[cur_y][cur_x] == 0: 
                visited[cur_y][cur_x] = 1
                queue.append((cur_x, cur_y, counter))

print(counter)

# =================================================================
# 4 6
# 101111
# 101010
# 101011
# 111011

# 15
# =================================================================
# 다른 사람의 풀이
from sys import stdin

n,m = map(int,input().split())

maze = [[0]*(m+2)]
for _ in range(n):
    maze.append([0]+list(map(int,list(stdin.readline().rstrip("\n"))))+[0])
maze.append([0]*(m+2))

que = [(1,1)]
maze[1][1] == 0
count = 1
while True:
    temp = []
    for node in que:
        i,j = node
        if maze[i+1][j] != 0:
            temp.append((i+1,j))
            maze[i+1][j] = 0

        if maze[i-1][j] != 0:
            temp.append((i-1,j))
            maze[i-1][j] = 0

        if maze[i][j+1] != 0:
            temp.append((i,j+1))
            maze[i][j+1] = 0

        if maze[i][j-1] != 0:
            temp.append((i,j-1))
            maze[i][j-1] = 0

    que = temp
    count += 1
    if (n,m) in temp:
        break

print(count)

# =================================================================