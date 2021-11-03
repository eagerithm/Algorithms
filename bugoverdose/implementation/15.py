# 로봇 청소기 (https://www.acmicpc.net/problem/14503)
# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
# - 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# - 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# - 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# - 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

N, M = map(int, input().split())

cur_row, cur_col, cur_dir = map(int, input().split())

graph = [] # 0: 빈 공간, 1: 벽, 2: 청소한 공간
for _ in range(N):
    graph.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
rotate_count = 0

cleaned = 1

while True:
    graph[cur_row][cur_col] = 2

    if rotate_count <= 4:
        cur_dir = (cur_dir+3)%4
        rotate_count += 1
        next_row = cur_row + dr[cur_dir]
        next_col = cur_col + dc[cur_dir]

        if graph[next_row][next_col] == 1: continue
        if graph[next_row][next_col] == 2: continue

        cleaned += 1
    else:
        cur_dir = (cur_dir+1)%4 # rotate_count == 4일 때는 못 갈 곳이면 회전X. 원상복귀.
        back_dir = (cur_dir+2)%4
        next_row = cur_row + dr[back_dir]
        next_col = cur_col + dc[back_dir]

        if graph[next_row][next_col] == 1: break

    cur_row = next_row
    cur_col = next_col
    rotate_count = 0

print(cleaned)

# =================================================================
# 11 10
# 7 4 0
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 0 0 0 0 1
# 1 0 1 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

# 57