# 팰린드롬? (https://www.acmicpc.net/problem/10942)
# 팰린드롬(palindrome)이란 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어

# 나의 정답 - 아직 체크 안해본 것만 직접 체크하고 캐슁 - 팰린드롬의 좌우를 k칸씩 지우면 마찬가지로 팰린드롬으로 캐슁
import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

graph = [[0]*(N+1) for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    if graph[a][b] == 1:
        print(1)
        continue

    if seq[a-1:b] != list(seq[a-1:b])[::-1]:
        print(0)
    else:
        print(1)
        while a <= b:
            graph[a][b] = 1
            a += 1
            b -= 1

#  =================================================================
# 시간초과
import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(1 if seq[a-1:b] == list(seq[a-1:b])[::-1] else 0)

#  =================================================================
# 시간초과
for _ in range(M):
    a, b = map(int, input().split())

    is_palindrome = True

    while a <= b:
        if seq[a] != seq[b]:
            is_palindrome = False
            break
        a += 1
        b -= 1
    
    print(1 if is_palindrome else 0)

# =================================================================