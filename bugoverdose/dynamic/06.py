# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

# 나의 정답
import sys

print = sys.stdout.write

w = {}

for a in range(0, 21):
    for b in range(0, 21):
        for c in range(0, 21):
            if a <= 0 or b <= 0 or c <= 0:
                w[(a,b,c)] = 1
            elif a < b and b < c:
                w[(a,b,c)] = w[(a, b, c-1)] + w[(a, b-1, c-1)] - w[(a, b-1, c)]
            else:
                w[(a,b,c)] = w[(a-1, b, c)] + w[(a-1, b-1, c)] + w[(a-1, b, c-1)] - w[(a-1, b-1, c-1)]

for line in sys.stdin:
    a, b, c = map(int, line.split())

    if a <= 0 or b <= 0 or c <= 0:
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = 1\n')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {w[20, 20, 20]}\n')
    else:
        print(f'w({a}, {b}, {c}) = {w[a, b, c]}\n')

# =================================================================