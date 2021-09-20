# 체스판 다시 칠하기 https://www.acmicpc.net/problem/1018
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 나의 정답
import sys

input = sys.stdin.readline

Y, X = map(int, input().split())
original = []
min_nums = []

for i in range(Y):
    original.append(input())

for start_y in range(Y-7):
    for start_x in range(X-7):
        BWBW = 0
        WBWB = 0

        for y in range(start_y, start_y+8):
            for x in range(start_x, start_x+8):
                if (x+y)%2 == 0:
                    if original[y][x] == "B":
                        WBWB += 1
                    else:
                        BWBW += 1
                else:
                    if original[y][x] == "W":
                        WBWB += 1
                    else:
                        BWBW += 1
        min_nums.append(min(BWBW, WBWB))

print(min(min_nums))

# =========================================

# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

# 12