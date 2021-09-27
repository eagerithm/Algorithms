# 계단 오르기 (https://www.acmicpc.net/problem/2579)
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

# 나의 정답
import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(int(input()))
else:
    steps = [int(input()) for _ in range(N)]
    dp1 = [steps[0], steps[0]+steps[1]] # prev O + cur O
    dp2 = [0, steps[1]]     # prev X + cur O
    dp3 = [steps[0], steps[0]] # prev O + cur X

    for idx in range(2, N):
        dp1.append(dp2[idx-1]+steps[idx])
        dp2.append(dp3[idx-1]+steps[idx])
        dp3.append(max(dp1[idx-1], dp2[idx-1]))

    print(max(dp1[-1], dp2[-1]))

# =================================================================
# 다른 사람의 풀이 - 배열 사용하지 않으므로 배열 셋업 과정 불필요 
from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())
for _ in range(n):
    pb = int(stdin.readline())
    d_0,d_1,d_2 = max(b,c),a+pb,b+pb
    a,b,c = d_0,d_1,d_2

print(max(d_2,d_1)) # d_0은 현재 계단을 밟지 않는 경우의 최대값

# =================================================================
# 10   - 10개의 계단
# 100  -
# 100  -
# 1    
# 1    -
# 100  
# 100  -
# 1    -
# 1000  
# 1000 -
# 1000 -

# 2302 - output
# =================================================================
# 6   - 6개의 계단
# 10 -
# 20 -
# 15
# 25 - 
# 10
# 20 - 

# 75 - output
# =================================================================