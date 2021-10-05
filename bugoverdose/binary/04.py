# 랜선 자르기 (https://www.acmicpc.net/problem/1654)
# 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

K, N = map(int, input().split())

originals = []
for _ in range(K):
    originals.append(int(input()))

right = max(originals) # 너무 짧은 것들은 사용할 필요 없으므로 min이 아니라 max
mid = (1+right+1)//2
left = 1
maximum = 1

while left <= right:
    counter = 0
    for o in originals:
        counter += o//mid
    if counter >= N:
        left = mid + 1
        if maximum < mid:
            maximum = mid
    else:
        right = mid - 1
    mid = (left+right+1)//2

print(maximum)

# ==================================================================
# 4 11
# 802
# 743
# 457
# 539

# 200
# ==================================================================
# min이 아니라 max로부터 시작해야 하는 이유 - 굳이 모든 랜선 활용할 필요 없음
# 4 5
# 500
# 1
# 1
# 1

# 100
# ==================================================================