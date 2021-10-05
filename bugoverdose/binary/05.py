# 나무 자르기 (https://www.acmicpc.net/problem/2805)
# 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
# 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 
# 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 
# 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

_, M = map(int, input().split())

trees = list(map(int, input().split()))

high = max(trees)
mid = (high+1)//2
low = 0
maximum = 0

while low <= high:
    wood = 0
    for t in trees:
        if t >= mid:
            wood += t - mid
    if wood >= M:
        maximum = max(mid, maximum)
        low = mid + 1
    else:
        high = mid - 1
    mid = (low+high+1)//2

print(maximum)

# ==================================================================