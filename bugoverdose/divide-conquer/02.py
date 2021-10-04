# 쿼드트리 (https://www.acmicpc.net/problem/1992)
# 흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

import sys

input = sys.stdin.readline

N = int(input()) # N은 언제나 2의 제곱수

area = []
for _ in range(N):
    area.append(list(input().strip()))

def divide(n, x, y):
    if n == 1: return area[y][x]
    
    d = n//2

    div2 = divide(d, x, y)
    div1 = divide(d, x+d, y)
    div3 = divide(d, x, y+d)
    div4 = divide(d, x+d, y+d)

    if div2 == div1 == div3 == div4: # (1010)(1010)(1010)(1010)의 경우 하나로 합칠 수 없음
        size = len(div1)
        sum = 0
        for n in list(div1):
            if n != "(" and n != ")":
                sum += int(n)
        if sum == size or sum == 0: # 1111 or 0000
            return div1

    return "(" + div2 + div1 + div3 + div4 + ")"

print(divide(N, 0, 0))

# ==================================================================
# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011

# ((110(0101))(0010)1(0001))