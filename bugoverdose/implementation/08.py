# Climbing the Leaderboard (https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem)

# 배열 자체는 변경 없이 포인터만 수정하는 방법
input()
ranks = [9999999999] + sorted(list(set(map(int, input().split()))), reverse = True)

N = int(input())
scores = list(map(int, input().split()))

idx = len(ranks)-1

for cur in range(N):
    cur_score = scores[cur]
    while idx > 0:
        if ranks[idx] > cur_score: break
        idx -= 1
    print(idx+1)

#  =================================================================
# 방법1
from collections import deque 

int(input())
ranks = deque(sorted(list(set(map(int, input().split())))))
N = int(input())
scores = list(map(int, input().split()))

for cur in range(N):
    cur_score = scores[cur]
    while True:
        if len(ranks) == 0:
            ranks.append(cur_score)
            break

        if ranks[0] < cur_score:
            ranks.popleft()
        elif ranks[0] > cur_score:
            ranks.appendleft(cur_score)
            break
        else:
            break

    print(len(ranks))

#  =================================================================