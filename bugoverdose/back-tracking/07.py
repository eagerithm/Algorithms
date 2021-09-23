# 스타트와 링크 
# https://www.acmicpc.net/problem/14889
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 

# 나의 정답


# =================================================================
# 시간 초과
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

stats = [[0]*(N+1)]
for line in range(N):     
    stats.append([0] + list(map(int, input().split())))
    
everyone = set([i for i in range(1, N+1)])
combs = list(map(set, combinations(everyone, N//2)))
visited = []
diffs = []

for comb in combs:
    team_a = comb
    team_b = everyone - comb
    team_a_stat = 0
    team_b_stat = 0

    if team_a in visited or team_b in visited: continue
    visited.append(team_a)

    for a1 in team_a:
        for a2 in team_a:
            if a1 >= a2: continue
            team_a_stat += stats[a1][a2] + stats[a2][a1]

    for b1 in team_b:
        for b2 in team_b:
            if b1 >= b2: continue
            team_b_stat += stats[b1][b2] + stats[b2][b1]

    diffs.append(abs(team_a_stat - team_b_stat))

print(min(diffs))

# =================================================================
# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0

# 2
# =================================================================