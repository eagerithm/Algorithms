# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
# 행렬 테두리 회전하기 (https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3)

def solution(row, col, queries):
    answer = []
    
    board = [[0]*(col+1)]
    for r in range(row):
        board.append([0]+[(r*col)+(i+1) for i in range(col)])
    
    for q in queries:
        min_val = row*col*99999
        left_top = (q[0], q[1]) 
        right_top = (q[0], q[3]) 
        right_bot = (q[2], q[3]) 
        left_bot = (q[2], q[1]) 
        
        cur_r = left_top[0]
        cur_c = left_top[1]
        queue = []
        while True:
            cur_val = board[cur_r][cur_c]
            if cur_r == left_top[0]:
                if cur_c < right_top[1]:
                    cur_c += 1
                else:
                    cur_r += 1
            elif cur_c == right_top[1]:
                if cur_r < right_bot[0]:
                    cur_r += 1
                else:
                    cur_c -= 1           
            elif cur_r == right_bot[0]:
                if left_bot[1] < cur_c:
                    cur_c -= 1
                else:
                    cur_r -= 1
            elif cur_c  == left_bot[1]:
                if left_top[0] < cur_r:
                    cur_r -= 1
            queue.append((cur_r, cur_c, cur_val))
            if min_val > cur_val:
                min_val = cur_val
            if cur_r == left_top[0] and cur_c == left_top[1]:
                break             
        for cur in queue:
            board[cur[0]][cur[1]] = cur[2]
        answer.append(min_val)
    return answer

# =================================================================
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        for i in range(c1, c2+1):
            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]

        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))

    return answer

# =================================================================
