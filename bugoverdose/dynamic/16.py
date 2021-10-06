# 파일 합치기 (https://www.acmicpc.net/problem/11066)
# 예를 들어, C1, C2, C3, C4가 연속적인 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 
# 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이때 비용 60이 필요하다. 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 
# 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이때 필요한 총 비용은 70+80+150=300 이다.
# 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.

# 주의: 서로 인접한 값들끼리만 합치는게 가능

# 정답 
import sys 

input = sys.stdin.readline 

for _ in range(int(input())):
    N = int(input())
    files = list(map(int, input().split()))    
    dp = [[0]*N for _ in range(N)] # dp의 index가 1씩 감소하기 때문에 2차원 배열 - 앞부분에 0이 추가되도록 

    # dp[i][j] : i번째부터 j번째 장까지 합쳤을 때의 단순 합계 - 마지막 두 장을 합칠 때의 비용은 언제나 동일
    for i in range(N-1): 
        dp[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, N):
            dp[i][j] = dp[i][j-1]  + files[j] 

    # dp[i][j] : i번째부터 j번째 장까지 합쳤을 때 가능한 누적 비용의 최소값
    # (i~k까지 더한 비용의 최솟값) + (k+1~j까지 더한 비용의 최솟값)들의 최소값을 순차적으로 dp에 더하기
    for unit in range(2, N): # 단위를 2, 3, 4으로 순차적으로 증가
        for i in range(N-unit): # (0, 2) (1, 3) (2, 4) ... | (0, 3) (1, 4) (2, 5) ... 
            j = i+unit # i번째부터 j번째 장까지의 누적 비용
            additional = []
            for k in range(i, j):
                additional.append(dp[i][k]+dp[k+1][j])
            dp[i][j] += min(additional)

    print(dp[0][N-1]) # 0~N-1번째 장까지의 누적 비용의 최소값

# ==================================================================
# wrong approach
# 40 30 
# 40 30 30 
# 40 30 30 50
# ==================================================================
# 오답 - 매번 가장 작은 2개를 합치기 - 서로 인접하지 않은 값들끼리도 합치는게 가능한 경우
import sys 
import heapq

input = sys.stdin.readline 

for _ in range(int(input())):
    N = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    sum = 0
    for _ in range(N-1):
        combined = heapq.heappop(files) + heapq.heappop(files)
        sum += combined
        heapq.heappush(files, combined)
        print(files)
    print(sum)
    
# ==================================================================