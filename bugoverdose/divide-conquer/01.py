# 색종이 만들기 (https://www.acmicpc.net/problem/2630)
# 전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.
# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 
# 출력: 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수

# 나의 정답
import sys

input = sys.stdin.readline

N = int(input()) # N은 2, 4, 8, 16, 32, 64, 128 중 하나

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
visited = [[False]*N for _ in range(N)]

blues = 0
whites = 0
visited_num = 0

a = N # 각 색종이의 변의 길이
b = 1 # b*b개로 잘린 색종이들

while visited_num < N*N:
    for y in range(b):
        for x in range(b): # b*b개의 색종이 각각에 대해 실행
            if visited[a*y][a*x] == True: continue

            total_sum = 0
            for i in range(a): # 각 색종이의 범위 a*a에 대해
                for j in range(a):
                    total_sum += paper[a*y+i][a*x+j]

            if total_sum != a*a and total_sum != 0: continue

            if total_sum == a*a:
                blues += 1
            elif total_sum == 0:
                whites += 1

            for i in range(a):  
                for j in range(a):
                    visited[a*y+i][a*x+j] = True 
            visited_num += a*a
    a = a//2
    b = b*2

print(whites)
print(blues)

# ==================================================================
# DFS - 가장 낮은 레벨부터 순차적으로 올라오는 방법
from sys import stdin

input = stdin.readline

def making_colored_paper(n, cp, x, y):
    if n == 1:
        return cp[x][y]

    cp1 = making_colored_paper(n // 2, cp, x, y)
    cp2 = making_colored_paper(n // 2, cp, x, y + n // 2)
    cp3 = making_colored_paper(n // 2, cp, x + n // 2, y)
    cp4 = making_colored_paper(n // 2, cp, x + n // 2, y + n // 2)

    # 1, 1, 1, 1 => 4개가 일치하면 하나로 합치기
    if cp1 == cp2 == cp3 == cp4 and len(cp1) == 1: 
        return cp1

    return cp1+cp2+cp3+cp4 # '10'+'10'+'00'+'01' 등의 경우

if __name__ == "__main__":
    N = int(input())
    paper = [input().split() for _ in range(N)] # 문자열 그대로 사용
    res = making_colored_paper(N, paper, 0, 0)
    print(res.count('0'), res.count('1'), sep='\n')

# ==================================================================