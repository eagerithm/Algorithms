# 날짜 계산 (https://www.acmicpc.net/problem/1476)
# 세 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# 1년은 1 1 1로 나타낼 수 있다. 1년이 지날 때마다 세 수는 모두 1씩 증가. 어떤 수가 범위를 넘어가는 경우에는 1이 됨.

A, B, C = map(int, input().split())

year = B

while True:
    if (year-1)%15 == A-1 and (year-1)%19 == C-1:
        break
    year += 28

print(year)

# =================================================================