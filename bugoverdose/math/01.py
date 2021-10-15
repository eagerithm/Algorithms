# https://www.acmicpc.net/problem/2775
# 특정 층의 특정 호수에 거주하는 인원 구하기
# 2층 1 4 10                    ex) 10 = 1+3+6 | 바로 아래층의 호수들의 인원 합 
# 1층 1 3  6 10 15 21 28   k=1  i*(i+1)/2 
# 0층 1 2  3  4  5  6  7   k=0  i 
 
# 나의 정답 
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    dp = [i for i in range(n+1)]
    
    for floor in range(k):
        for room in range(2, n+1):
            dp[room] += dp[room-1]

    print(dp[n])

# =========================================
# 성능 개선
import sys

input = sys.stdin.readline
people = [[i for i in range(15)]] 

for f in range(1, 15):
    people.append([0]*15)

for f in range(1, 15):
    for r in range(1, 15):
        people[f][r] = sum(people[f-1][:r+1])

for i in range(int(input())):
    floor = int(input())
    room = int(input())
    print(people[floor][room])

# =========================================
# 다른 사람의 풀이 - 메모이제이션
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])

# =========================================