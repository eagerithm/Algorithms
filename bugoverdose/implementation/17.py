# 테트로미노 (https://www.acmicpc.net/problem/14500)
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

# 방법1
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

max_sum = 0

# [][]
# [][]
for r in range(N-1):
    for c in range(M-1):
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r][c+1]+graph[r+1][c+1], max_sum)

# [][][][]
for r in range(N-3):
    for c in range(M):
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r+2][c]+graph[r+3][c], max_sum)
for r in range(N):
    for c in range(M-3):
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r][c+2]+graph[r][c+3], max_sum)

# [][][]   # [][][]   # [][]     #   [][]  # [][][]
# []       #     []   #   [][]   # [][]    #   []
for r in range(N-1):
    for c in range(M-2):
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r][c+2]+graph[r+1][c], max_sum)
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r][c+2]+graph[r+1][c+2], max_sum)
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r+1][c+1]+graph[r+1][c+2], max_sum)
        max_sum = max(graph[r+1][c]+graph[r+1][c+1]+graph[r][c+1]+graph[r][c+2], max_sum)
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r][c+2]+graph[r+1][c+1], max_sum)

        # 180도 회전 : 1,2,5번째만
        max_sum = max(graph[r+1][c]+graph[r+1][c+1]+graph[r+1][c+2]+graph[r][c+2], max_sum)
        max_sum = max(graph[r+1][c]+graph[r+1][c+1]+graph[r+1][c+2]+graph[r][c], max_sum)
        max_sum = max(graph[r+1][c]+graph[r+1][c+1]+graph[r+1][c+2]+graph[r][c+1], max_sum)

# [][][]   # [][][]   # [][]     #   [][]  # [][][]
# []       #     []   #   [][]   # [][]    #   []
for r in range(N-2):
    for c in range(M-1):
        # 시계방향
        max_sum = max(graph[r][c]+graph[r][c+1]+graph[r+1][c+1]+graph[r+2][c+1], max_sum)
        max_sum = max(graph[r][c+1]+graph[r+1][c+1]+graph[r+2][c+1]+graph[r+2][c], max_sum)
        max_sum = max(graph[r][c+1]+graph[r+1][c+1]+graph[r+1][c]+graph[r+2][c], max_sum)
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r+1][c+1]+graph[r+2][c+1], max_sum)
        max_sum = max(graph[r+1][c]+graph[r][c+1]+graph[r+1][c+1]+graph[r+2][c+1], max_sum)

        # 반시계방향
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r+2][c]+graph[r+2][c+1], max_sum)
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r+2][c]+graph[r][c+1], max_sum)
        max_sum = max(graph[r][c]+graph[r+1][c]+graph[r+2][c]+graph[r+1][c+1], max_sum)

print(max_sum)

# =================================================================
# 방법2 : 느리지만 확장성 지님
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 핵심: 특정 기준점을 중심으로 시계방향으로 돌리기
# [][][][]  # [][]   # [][][]   # [][][]   # [][]     #   [][]  # [][][]
            # [][]   # []       #     []   #   [][]   # [][]    #   []
patterns = [ 
    ((0, 1), (0, 2), (0, 3)),  
    ((1, 0), (2, 0), (3, 0)),  
    ((0, 1), (1, 0), (1, 1)),  
    ((1, 0), (2, 0), (2, 1)),  
    ((1, 0), (2, 0), (2, -1)),  
    ((0, -1), (1, 0), (2, 0)),  
    ((0, 1), (1, 0), (2, 0)),  
    ((1, 0), (1, 1), (1, 2)),  
    ((0, 1), (0, 2), (-1, 2)),  
    ((0, 1), (0, 2), (1, 2)),  
    ((0, 1), (0, 2), (1, 0)),  
    ((1, 0), (0, 1), (-1, 1)),  
    ((1, 0), (1, 1), (2, 1)),  
    ((0, 1), (-1, 1), (-1, 2)),  
    ((0, 1), (1, 1), (1, 2)),  
    ((0, 1), (1, 1), (0, 2)),  
    ((0, 1), (-1, 1), (0, 2)),  
    ((-1, 0), (-1, -1), (-2, 0)),  
    ((-1, 0), (-1, 1), (-2, 0)),
]

max_sum = 0

for row in range(N):
    for col in range(M):
        start_num = graph[row][col]
        for pattern in patterns:
            new_sum = start_num
            visited_all = True
            for dir_row, dir_col in pattern:
                next_row = row + dir_row
                next_col = col + dir_col
                if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
                    visited_all = False
                    break
                new_sum += graph[next_row][next_col]
            if visited_all:
                max_sum = max(max_sum, new_sum)

print(max_sum)

# =================================================================