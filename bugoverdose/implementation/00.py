# 2차원 배열 내 좌표 이동
# https://ldh-developer.tistory.com/17

N = int(input())

visited = [[False]*N for _ in range(N)]

cur_y = 0 # 가장 왼쪽 위를 (0,0)
cur_x = 0 # 가장 오른쪽 아래를 (N-1, N-1)로 간주

cur_dir = 0
dy = [1, -1, 0, 1] # 하, 우상(반복), 우, 좌하(반복)
dx = [0, 1, 1, -1]

route = [(0, 0)]

while True:
    if cur_y == N-1 and cur_x == N-1: break
    next_y = cur_y + dy[cur_dir]
    next_x = cur_x + dx[cur_dir]
    if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N or visited[next_y][next_x]: 
        cur_dir = (cur_dir+1)%4
        continue

    if cur_dir == 0 or cur_dir == 2: # 언제나 한칸만 이동하는 경우
        cur_dir = (cur_dir+1)%4 # cur_dir == 1 or 3일때는 일단 그대로 쭉 가도록

    visited[next_y][next_x] = True
    route.append((next_y, next_x))

    cur_y = next_y
    cur_x = next_x

print(route)

# =================================================================