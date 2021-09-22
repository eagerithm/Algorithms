# N-Queen
# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 나의 정답
N = int(input())
answer = []
stack = [[i] for i in range(1,N+1)] # index=y, value=x

def dfs(answer, possibles, queen_set):
    queen_set = possibles.pop()

    length = len(queen_set)

    if length == N:
        answer.append(queen_set)
        queen_set = []
        return answer

    for i in range(1,N+1):
        if i in queen_set: continue
        can_go = True
        
        for idx in range(length):
            if i == queen_set[idx]+length-idx or i == queen_set[idx]-length+idx:
                can_go = False
                break
        if can_go:
            possibles.append(queen_set + [i])
            answer = dfs(answer, possibles, queen_set)

    if len(possibles) == 0:
        return answer
    else:
        return dfs(answer, possibles, queen_set)

answer = dfs(answer, stack, [])

print(len(answer))

# =================================================================
# 다른 사람의 풀이 - NxN 보드를 배열 한개로 DP 방식
def nQueen(i):
    global count
    if i == N:
        count += 1
        return

    # row 행의 각 열(col)을 검사
    for col in range(N):
        # 상하 열에 다른 퀸이 존재하지 않음: row[col] == 0
        # \ 방향 대각선에 다른 퀸이 존재하지 않음: left[i + col] == 0
        # / 방향 대각선에 다른 퀸이 존재하지 않음: right[i - col + N-1] == 0
        if row[col] + left[i + col] + right[i - col + N-1] == 0:
            row[col] = 1
            left[i + col] = 1
            right[i - col + N-1] = 1

            nQueen(i+1)

            row[col] = 0
            left[i + col] = 0
            right[i - col + N - 1] = 0


N = int(input())
count = 0
# 퀸이 움직일 수 있는 이동 경우 3가지
row = [0 for _ in range(N)]             # 각 행
left = [0 for _ in range(2*N-1)]        # \ 방향 대각선
right = [0 for _ in range(2*N-1)]       # / 방향 대각선

nQueen(0)
print(count)

# =================================================================