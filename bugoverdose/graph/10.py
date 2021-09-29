# 숨바꼭질 (https://www.acmicpc.net/problem/1697)
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 나의 정답 - visited를 dictionary로 만들어야 시간초과 예방됨
N, K = map(int, input().split())

time = 0
queue = [N]
visited = [False]*100001 
visited[N] = True

while queue:
    if K in queue: break
    next = []
    while queue:
        X = queue.pop()
        if 0 <= X-1 and visited[X-1] == False:
            next.append(X-1)
            visited[X-1] = True
        if X+1 <= 100000 and visited[X+1] == False:
            next.append(X+1)
            visited[X+1] = True
        if 2*X <= 100000 and visited[2*X] == False:
            next.append(2*X)
            visited[2*X] = True

    queue = next
    time += 1

print(time)

# =================================================================
# 메모리 초과 - X+1 X-1 반복하면서 제자리 왔다갔다거리며 동일한 과정 3배씩 무한반복하게 됨
N, K = map(int, input().split())

queue = [N]
time = 0

while queue:
    if K in queue: break
    next = []
    while queue:
        X = queue.pop()
        if K in [X-1, X+1, 2*X]: break
        if 0 <= X-1:
            next.append(X-1)
        if X+1 <= 100000:
            next.append(X+1)
        if 2*X <= 100000:
            next.append(2*X)

    queue = next
    time += 1

print(time)

# =================================================================