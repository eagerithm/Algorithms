# 스티커 (https://www.acmicpc.net/problem/9465)
# 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
# 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    dp = [0, 0, 0] # 위 선택, 아래 선택, 무선택시 최대 누적값

    for idx in range(N):
        prev_up, prev_down, prev_none = dp
        choose_up = stickers[0][idx]
        choose_down = stickers[1][idx]

        new_up = max(prev_down, prev_none) + choose_up
        new_down = max(prev_up, prev_none) + choose_down
        new_none = max(prev_up, prev_down)
        dp = [new_up, new_down, new_none]

    print(max(dp))

#  =================================================================