# 빗물 (https://www.acmicpc.net/problem/14719)

H, W = map(int, input().split())
block = list(map(int, input().split()))
prev = []
rain = 0

for idx in range(W): 
    cur = block[idx]
    if len(prev) == 0: # 이전 단계까지 빗물들 다 계산됨
        if cur != 0: 
            prev.append(cur)
        continue
    
    if prev[0] <= cur: # 맨왼쪽 이상의 높이가 등장했으면 그 위치까지 전부 빗물 고였다고 간주
        high = prev[0]
        while prev:
            low = prev.pop()
            rain += high-low # 자기자신 혹은 자신과 동일한 높이들은 안고였으므로 자동으로 0 대입
    
    prev.append(cur)

# 중간에 최대높이가 있고 그 이후에 그보다 낮은 높이들만 나온 경우, 위의 과정 좌우 반전
block = prev[::-1]
prev = []

for idx in range(len(block)): 
    cur = block[idx]
    if len(prev) == 0: 
        if cur != 0: 
            prev.append(cur)
        continue
    
    if prev[0] <= cur: 
        high = prev[0]
        while prev:
            low = prev.pop()
            rain += high-low

    prev.append(cur)
    
print(rain)

# =================================================================