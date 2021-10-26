# Queen's Attack II (https://www.hackerrank.com/challenges/queens-attack-2/problem)

# 각 장애물에 대해 갈 수 있는 거리값들 갱신: O(N)
N, k = map(int, input().split())
row, col = map(int, input().split())

directions = []
directions.append(N-row)
directions.append(min(N-row, N-col))
directions.append(N-col)
directions.append(min(row-1, N-col))
directions.append(row-1)
directions.append(min(row-1, col-1))
directions.append(col-1)
directions.append(min(N-row, col-1))

for _ in range(k):
    o_row, o_col = map(int, input().split())

    if col == o_col:
        if row < o_row:
            directions[0] = min(directions[0], o_row-row-1)
        elif o_row < row:
            directions[4] = min(directions[4], row-o_row-1)

    elif row == o_row:
        if col < o_col:
            directions[2] = min(directions[2], o_col-col-1)
        elif o_col < col:
            directions[6] = min(directions[6], col-o_col-1)

    else:
        if abs(o_col-col) != abs(o_row-row): continue
        if o_col > col and o_row > row:
            directions[1] = min(directions[1], abs(o_row-row)-1, abs(o_col-col)-1)
        elif o_col > col and o_row < row:
            directions[3] = min(directions[3], abs(o_row-row)-1, abs(o_col-col)-1)
        elif o_col < col and o_row < row:
            directions[5] = min(directions[5], abs(o_row-row)-1, abs(o_col-col)-1)
        elif o_col < col and o_row > row:
            directions[7] = min(directions[7], abs(o_row-row)-1, abs(o_col-col)-1)

print(sum(directions))

#  =================================================================
# Runtime Error : 시간초과 혹은 메모리초과로 추정
N, k = map(int, input().split())
row, col = map(int, input().split())

board = [[False]*(N+1) for _ in range(N+1)]
for _ in range(k):
    o_row, o_col = map(int, input().split())
    board[o_row][o_col] = True

counter = 0

for idx in range(1, N):
    if row+idx > N or board[row+idx][col]: break
    counter += 1

for idx in range(1, N):
    if row+idx > N or col+idx > N or board[row+idx][col+idx]: break
    counter += 1

for idx in range(1, N):
    if col+idx > N or board[row][col+idx]: break
    counter += 1

for idx in range(1, N):
    if row-idx < 1 or col+idx > N or board[row-idx][col+idx]: break
    counter += 1

for idx in range(1, N):
    if row-idx < 1 or board[row-idx][col]: break
    counter += 1

for idx in range(1, N):
    if row-idx < 1 or col-idx < 1 or board[row-idx][col-idx]: break
    counter += 1

for idx in range(1, N):
    if col-idx < 1 or board[row][col-idx]: break
    counter += 1

for idx in range(1, N):
    if row+idx > N or col-idx < 1 or board[row+idx][col-idx]: break
    counter += 1

print(counter)

#  =================================================================