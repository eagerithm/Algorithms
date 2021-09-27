# 최소공배수 (https://www.acmicpc.net/problem/1934)

# 유클리드 호제법
# 1071과 1029의 최대공약수를 구하면,
# 1071은 1029로 나누어떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
# 1029는 42로 나누어떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
# 42는 21로 나누어떨어진다. 따라서, 최대공약수는 21이다.

# 나의 정답
import sys

input = sys.stdin.readline

def get_mcf(bigger,smaller):
    mcf = smaller
    if bigger%smaller != 0:
        mcf = get_mcf(smaller, bigger%smaller)
    return mcf

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    mcf = get_mcf(max(A,B), min(A,B))
    print(A*B//mcf)

# =================================================================
# 일반적인 풀이
import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())

    MCF = 1

    for num in range(2, min(A, B)+1):
        if A%num == 0 and B%num == 0:
            MCF = num

    print(A*B//MCF)

# =================================================================
# 3
# 1 45000
# 6 10
# 13 17

# 45000
# 30
# 221