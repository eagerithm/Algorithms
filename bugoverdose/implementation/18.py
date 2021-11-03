# 뱀 (https://www.acmicpc.net/problem/3190)
# 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

N = int(input())
graph = [[0]*N for _ in range(N)]

for _ in range(int(input())):
    r, c = map(int, input().split()) # 1행 1열
    graph[r-1][c-1] = 10             # 0행 0열

cur_dir = 0
dir_row = [0, 1, 0, -1]
dir_col = [1, 0, -1, 0]

rotations = [(0, 0)]

for _ in range(int(input())):
    time, direction = input().split()

    if direction == "L":
        cur_dir = (cur_dir+3)%4
    elif direction == "D":
        cur_dir = (cur_dir+1)%4

    rotations.append((int(time), cur_dir))

snake_rows = [0]
snake_cols = [0]
graph[0][0] = 1 # 뱀

time = 0

while True:
    if len(rotations) > 0 and rotations[0][0] == time:
        cur_dir = rotations.pop(0)[1]
    
    time += 1

    next_row = snake_rows[-1] + dir_row[cur_dir]
    next_col = snake_cols[-1] + dir_col[cur_dir]

    if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N: break
    if graph[next_row][next_col] == 1: break

    if graph[next_row][next_col] != 10:
        graph[snake_rows.pop(0)][snake_cols.pop(0)] = 0

    graph[next_row][next_col] = 1
    snake_rows.append(next_row)
    snake_cols.append(next_col)

print(time)

# =================================================================