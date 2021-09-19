# https://www.acmicpc.net/problem/2839
# 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# -5 + 3 + 3 = 1
# -5 + 3     = -2 
#    - 3     = -3
 
# 나의 정답 
N = int(input())

fives = N//5
threes = 0
dif = N%5
possible = True

while dif != 0:
    if dif >= 3:
        threes += 1
        dif -= 3
    elif dif > 0:
        if fives == 0: 
            possible = False
            break
        fives -= 1
        threes += 2
        dif -= 1
    elif dif >= -2:
        if fives == 0: 
            possible = False
            break
        fives -= 1
        threes += 1
        dif += 2
    else:
        threes += 1
        dif += 3

if possible:
    print(fives + threes)
else:
    print(-1)

# =========================================
# 다른 사람의 풀이 
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0: # 3으로 나눠질 때까지 계속 5킬로 봉지 1개씩 빼기
    if b%3 == 0:
        c = b//3
        
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)

# =========================================