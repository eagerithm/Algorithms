# 치킨 배달 (https://www.acmicpc.net/problem/15686)
# 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 
# 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

from itertools import combinations

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

chicken_pos = []
house_pos = {}

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            house_pos[(y,x)] = []
        elif graph[y][x] == 2:
            chicken_pos.append((y,x))

chicken_num = len(chicken_pos)

for key in house_pos.keys():
    (y, x) = key
    for idx in range(chicken_num):
        cy, cx = chicken_pos[idx]
        house_pos[key].append(abs(cy-y)+abs(cx-x))

min_sum_len = 999999999999999999

for chicken_idxs in combinations([i for i in range(chicken_num)], M):
    sum_len = 0
    for key in house_pos.keys():
        min_house_len = 9999999999999 
        for idx in chicken_idxs:
            min_house_len = min(house_pos[key][idx], min_house_len)
        sum_len += min_house_len
    min_sum_len = min(sum_len, min_sum_len)

print(min_sum_len)

# =================================================================