# 전깃줄 (https://www.acmicpc.net/problem/2565)

# 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 
# 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

# 중요: 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

import sys

input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort(key=lambda x:(x[0], x[1]))

last_ends = [0]
for _, cur_end in lines:
    if last_ends[-1] < cur_end:
        last_ends.append(cur_end)
    else:
        prev_idx = -2
        while last_ends[prev_idx] > cur_end:
            prev_idx -= 1
        last_ends[prev_idx+1] = cur_end

print(N - len(last_ends) + 1)

# =================================================================