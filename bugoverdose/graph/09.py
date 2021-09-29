# 토마토 - 상하좌우앞뒤의 다른 토마토들이 하나씩 익어갈 때 모든 토마토가 익을 때까지 걸리는 시간 구하기

# BFS의 특징: 각 정점을 최단경로로 방문

# 2차원 : https://www.acmicpc.net/problem/7576
import sys

input = sys.stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

X, Y = map(int, input().split())

days = 0 
queue = []
tomato = []

for y in range(Y):
    row = list(map(int, input().split()))
    tomato.append(row)
    for x in range(X):
        if row[x]==1:
            queue.append((x,y))

while queue:
    next = []
    effected = False
    while queue:
        x, y = queue.pop()
        for i in range(4):
            cur_x = x+dx[i]
            cur_y = y+dy[i]
            if 0 <= cur_x < X and 0 <= cur_y < Y:
                if tomato[cur_y][cur_x] == 0: 
                    tomato[cur_y][cur_x] = 1
                    next.append((cur_x, cur_y))
                    effected = True
    if effected:
        days += 1
    queue = next

possible = True

for y in range(Y):
    if 0 in tomato[y]:
        possible = False
        break
print(days if possible else -1)

# =================================================================
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 8
# =================================================================
# 3차원 : https://www.acmicpc.net/problem/7569
import sys

input = sys.stdin.readline

dx = [0,0,-1,1,0,0] # 상하좌우앞뒤
dy = [0,0,0,0,-1,1]
dz = [1,-1,0,0,0,0]

X, Y, Z = map(int, input().split())

days = 0
queue = []
tomato = []

for z in range(Z):
    tomato.append([])
    for y in range(Y):
        row = list(map(int, input().split()))
        tomato[z].append(row)
        for x in range(X):
            if row[x]==1:
                queue.append((x,y,z))

while queue:
    next = []
    effected = False
    while queue:
        x, y, z = queue.pop()
        for i in range(6):
            cur_x = x+dx[i]
            cur_y = y+dy[i]
            cur_z = z+dz[i]
            if 0 <= cur_x < X and 0 <= cur_y < Y and 0 <= cur_z < Z:
                if tomato[cur_z][cur_y][cur_x] == 0: 
                    tomato[cur_z][cur_y][cur_x] = 1
                    next.append((cur_x, cur_y, cur_z))
                    effected = True
    if effected:
        days += 1
    queue = next

possible = True

for z in range(Z):
    for y in range(Y):
        if 0 in tomato[z][y]:
            possible = False
            break
print(days if possible else -1)

# =================================================================
# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0

# 4
# =================================================================