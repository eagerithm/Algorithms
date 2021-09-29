# 벽 부수고 이동하기 (https://www.acmicpc.net/problem/2206)
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 중요: 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 나의 정답 - 벽뚫었는지의 여부에 따른 2가지 visited 활용 - 3차원 배열 사용안하고 2개 사용해도 될 듯 함.
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1] 
dy = [1,-1,0,0] 

Y, X = map(int, input().split())

maze = [[0]*(X+1)]
for _ in range(Y):
    maze.append([0] + list(map(int, list(input().strip()))))

# visited 자체에 벽뚫었는지의 여부 + 몇번 거쳐왔는지의 여부 등록
visited = [[[0]*2 for _ in range(X+1)] for _ in range(Y+1)] 
visited[1][1][1] += 1 # visited[y][x][1] 사용 중이므로 아직 벽뚫기 가능한 상태에서의 counter

queue = deque([(1,1,1)]) # (x,y,벽뚫기 찬스 존재하면 1 아니면 0)

answer = -1

while queue:
    (x, y, w) = queue.popleft()

    if x==X and y==Y:
        answer = visited[y][x][w]
        break

    for i in range(4):
        xi = x+dx[i]
        yi = y+dy[i]
        if 1 <= xi <= X and 1 <= yi <= Y:
            if maze[yi][xi] == 1 and w == 1: # w==1: 아직 벽뚫기 가능
                visited[yi][xi][0] = visited[y][x][1] + 1 # 벽뚫기 불가능한 w==0로 옮기기
                queue.append((xi,yi,0))
            elif maze[yi][xi] == 0 and visited[yi][xi][w] == 0: # counter가 0이면 아직 도달한 적이 없음. 중복 제거. (w에 의해 벽뚫었는지의 여부 구분 가능)
                visited[yi][xi][w] = visited[y][x][w] + 1 # 벽뚫었는지의 여부와 무관하게 그대로 counter만 1 증가시키기
                queue.append((xi,yi,w))
print(answer)

# =================================================================
# 5 5
# 00000
# 11110
# 00000
# 01111
# 00010

# 9
# =================================================================
# 오답 - 벽을 부수고 앞질러 지니간 경로가 visited=True로 공유되면서 벽을 부수지 않고 늦게 도달한 경우가 도달할 수 없게 됨!!!
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1] 
dy = [1,-1,0,0] 

Y, X = map(int, input().split())

maze = [[0]*(X+1)]
visited = [[False]*(X+1) for _ in range(Y+1)]

for _ in range(Y):
    maze.append([0] + list(map(int, list(input().strip()))))

queue = deque([(1,1,True)]) # (x,y,벽부수기 1회 가능 여부)
visited[1][1] = True
counter = 1

while queue:
    if visited[Y][X] == True:
        break
    next = deque()
    while queue:
        (x, y, can_break) = queue.popleft()
        for i in range(4):
            xi = x+dx[i]
            yi = y+dy[i]
            if 1 <= xi <= X and 1 <= yi <= Y and visited[yi][xi] == False:
                if maze[yi][xi] == 1 and can_break == True:
                    visited[yi][xi] = True
                    next.append((xi, yi, False)) # 다른 좌표에서도 사용해야 하므로 can_break 변수 변경금지
                elif maze[yi][xi] == 0:
                    visited[yi][xi] = True
                    next.append((xi, yi, can_break))
    counter += 1
    queue = next

if visited[Y][X] == True:
    print(counter)
else:
    print(-1)

# =================================================================
# 메모리 초과 - 가능한 모든 경로들에 대해 개별적으로 visited 정보 관리하면 메모리 초과
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1] 
dy = [1,-1,0,0] 

Y, X = map(int, input().split())

maze = [[0]*(X+1)]

for _ in range(Y):
    maze.append([0] + list(map(int, list(input().strip()))))

queue = deque([(1,1,True, [(1,1)])]) # (x,y,벽부수기 1회 가능 여부, 자신이 지나온 경로)
counter = 1
reached_end = False

if X==1 and Y==1:
    reached_end = True

while queue:
    if reached_end: break
    next = deque()
    while queue:
        (x, y, can_break, visited) = queue.popleft()
        for i in range(4):
            xi = x+dx[i]
            yi = y+dy[i]
            if 1 <= xi <= X and 1 <= yi <= Y and (xi,yi) not in visited:
                if maze[yi][xi] == 1 and can_break == True:
                    next.append((xi, yi, False, visited+[(xi,yi)])) # 다른 좌표에서도 사용해야 하므로 can_break 변수 변경금지
                elif maze[yi][xi] == 0:
                    next.append((xi, yi, can_break, visited+[(xi,yi)]))
                if xi == X and yi == Y:
                    reached_end = True
    counter += 1
    queue = next

if reached_end:
    print(counter)
else:
    print(-1)

# =================================================================