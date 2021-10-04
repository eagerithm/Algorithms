# 종이의 개수 (https://www.acmicpc.net/problem/1780)
# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

paper_num = [0,0,0]

def divide(n, x, y):
    if n == 1: return paper[y][x]

    length = n//3
    results = []
    for i in range(3):
        for j in range(3):
            results.append(divide(length, x+length*i, y+length*j))
    
    is_same = True
    a, b, c = 0, 0, 0
    for r in results:
        if r != results[0]:
            is_same = False
        if r == -1:
            a += 1
        elif r == 0:
            b += 1
        elif r == 1:
            c += 1

    if is_same and results[0] != -2:
        return results[0]
    else:
        paper_num[0] += a 
        paper_num[1] += b 
        paper_num[2] += c 
        return -2
    
final_result = divide(N, 0, 0)

if final_result == -1:
    paper_num[0] += 1
elif final_result == 0:
    paper_num[1] += 1
elif final_result == 1:
    paper_num[2] += 1

for p in paper_num:
    print(p)

# ==================================================================
# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1

# 10
# 12
# 11