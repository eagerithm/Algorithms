# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임 (https://programmers.co.kr/learn/courses/30/lessons/64061)

def solution(board, moves):
    queue_num = len(board[0])
    board_queue = [[] for _ in range(queue_num)]
    for b in board:
        for idx in range(queue_num):
            if b[idx] != 0:
                board_queue[idx].append(b[idx])
    
    stack = []
    answer = 0
    for m in moves:
        idx = m-1
        if len(board_queue[idx]) == 0: continue        
        new = board_queue[idx].pop(0)
        if len(stack) > 0 and stack[-1] == new:
            stack.pop()
            answer += 2
            continue
        stack.append(new)

    return answer
    
# ==========================================================