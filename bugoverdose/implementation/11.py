# Organizing Containers of Balls (https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem)
# 각 컨테이너에 오직 1가지 종류의 공들만 오도록 할 수 있는가?

# 원리 찾아내기
for _ in range(int(input())):
    N = int(input())
    containers = []
    ball_nums = []
    container_sizes = []

    for _ in range(N):
        container = list(map(int, input().split()))
        container_sizes.append(sum(container))
        containers.append(container)

    for ball_idx in range(N):
        ball_num = 0
        for container_idx in range(N):
            ball_num += containers[container_idx][ball_idx]
        ball_nums.append(ball_num)

    print("Possible" if sorted(ball_nums) == sorted(container_sizes) else "Impossible")

#  =================================================================