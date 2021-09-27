# 주유소 (https://www.acmicpc.net/problem/13305)
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
# 나의 정답
N = int(input()) - 1 # 도시의 개수-1 = 도시 간 거리의 개수
distances = list(map(int, input().split())) # 인접한 두 도시를 연결하는 도로의 길이
oil_price = list(map(int, input().split())) # 주유소의 리터당 가격

cost = 0
min_price = oil_price[0]

for idx in range(N):
    if oil_price[idx] < min_price:
        min_price = oil_price[idx]
    cost += min_price * distances[idx]

print(cost)


# =================================================================