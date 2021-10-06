# 양팔저울 (https://www.acmicpc.net/problem/2629)
# 첫째 줄에는 추의 개수가 자연수로 주어진다. 추의 개수는 30 이하이다. 둘째 줄에는 추의 무게들이 자연수로 가벼운 것부터 차례로 주어진다. 같은 무게의 추가 여러 개 있을 수도 있다. 추의 무게는 500g이하이며, 입력되는 무게들 사이에는 빈칸이 하나씩 있 다. 세 번째 줄에는 무게를 확인하고자 하는 구슬들의 개수가 주어진다. 확인할 구슬의 개수는 7이하이다. 네 번째 줄에는 확인하고자 하는 구슬들의 무게가 자연수로 주어지며, 입력되는 무게들 사이에는 빈 칸이 하나씩 있다. 확인하고자 하는 구슬의 무게는 40,000보다 작거나 같은 자연수이다.
# 주어진 각 구슬의 무게에 대하여 확인이 가능하면 Y, 아니면 N 을 차례로 출력한다. 

# 냅색 알고리즘은 담을 수 있는 물건이 나눌 수 있냐 없냐에 따라 나눈다.
# 담을 수 있는 물건이 나누어 질 때(설탕 몇 g 등): 분할가능 배낭문제(Fractional Knapsack Problem)
# 담을 수 있는 물건이 나누어 질 수 없을 때(담는다 or 안담는다): 0-1 배낭문제(0-1 Knapsack Problem)

# 나의 정답 
N = int(input())
weights = list(map(int, input().split()))
input()
marbles = list(map(int, input().split()))

possible = [0]*40001

combinations = []

for w in weights:
    for c in list(combinations):
        if possible[c+w] == 0:
            combinations.append(c+w) 
            possible[c+w] = 1       
        if possible[abs(c-w)] == 0:
            combinations.append(abs(c-w))
            possible[abs(c-w)] = 1
    if possible[w] == 0:
        combinations.append(w)  
        possible[w] = 1

for m in marbles:
    print("Y" if possible[m] == 1 else "N", end=" ")

# ==================================================================
# 2
# 1 4
# 2
# 3 2

# Y N
# ==================================================================
# 다른 사람의 풀이 - set을 통한 중복제거
input()
s = []
for k in map(int, input().split(' ')):
    for i in range(len(s)):
        s.append(k+s[i])
        s.append(abs(k-s[i]))
    s.append(k)
    s=list(set(s))
input()
for k in map(int, input().split(' ')):
    print("Y" if k in s else "N",end=' ')
    
# ==================================================================