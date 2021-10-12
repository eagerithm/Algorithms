# 스도쿠 (https://www.acmicpc.net/problem/2580) 

# 나의 정답 - DFS
import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

zeros = []
for cur_y in range(9):
    for cur_x in range(9):
        if board[cur_y][cur_x] == 0:
            zeros.append((cur_y, cur_x, [i for i in range(1, 10)]))

def dfs(board, idx):
    is_full = len(zeros) == idx
    if not is_full:
        cur_y, cur_x, possibles = zeros[idx]
        for p in possibles:
            go_back = False
            for i in range(9):
                if board[cur_y][i] == p or board[i][cur_x] == p:
                    go_back = True
            if go_back: continue
            
            start_y = cur_y//3 * 3
            start_x = cur_x//3 * 3
            for y in range(start_y, start_y+3):
                for x in range(start_x, start_x+3):
                    if board[y][x] == p:
                        go_back = True
            if go_back: continue
            
            board[cur_y][cur_x] = p
            board, finished = dfs(board, idx+1)
            if finished:
                return board, finished
            board[cur_y][cur_x] = 0

    return board, is_full

board, _ = dfs(board, 0)

for row in board:
    print(" ".join(map(str, row)))

# =================================================================
# 다른 사람의 풀이
sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)

# =================================================================
# 시간초과 - 입력에 따라 해결 불가능
import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

targets = deque()
for cur_y in range(9):
    for cur_x in range(9):
        if board[cur_y][cur_x] == 0:
            targets.append((cur_y, cur_x, set([i for i in range(1, 10)])))

while targets:
    cur_y, cur_x, possibles = targets.popleft()

    possibles = possibles - set(board[cur_y])

    if len(possibles) > 1:
        impossibles = []
        for y in range(9):
            if board[y][cur_x] != 0:
                impossibles.append(board[y][cur_x])
        possibles = possibles - set(impossibles)

    if len(possibles) > 1:
        impossibles = []
        start_y = cur_y//3 * 3
        start_x = cur_x//3 * 3
        for y in range(start_y, start_y+3):
            for x in range(start_x, start_x+3):
                if board[y][x] != 0:
                    impossibles.append(board[y][x])
        possibles = possibles - set(impossibles)

    if len(possibles) == 1:
        board[cur_y][cur_x] = list(possibles)[0]
    else:
        targets.append((cur_y, cur_x, possibles))

for row in board:
    print(" ".join(map(str, row)))

# =================================================================
