# 냅색문제 (https://www.acmicpc.net/problem/1450)
# 최대 C만큼의 무게를 넣을 수 있는 가방에 N개의 물건을 넣는 방법의 수를 구하는 프로그램을 작성하시오.

# Meet in the middle 알고리즘
# 반으로 나누어 작업함으로써 10^10 => 10^5 + 10^5로 급감시키는 방법

# 나의 정답
N, limit = map(int, input().split())
weights = list(map(int, input().split()))

middle = len(weights)//2

a_weights = weights[:middle]
a_sums = [0] # 아무것도 선택하지 않은 경우
for cur in a_weights:
    if cur <= limit:
        for prev_sum in list(a_sums):
            if prev_sum + cur <= limit:
                a_sums.append(prev_sum + cur)

b_weights = weights[middle:]
b_sums = [0] 
for cur in b_weights:
    if cur <= limit:
        for prev_sum in list(b_sums):
            if prev_sum + cur <= limit:
                b_sums.append(prev_sum + cur)

answer = 0
for a_sum in a_sums:
    for b_sum in b_sums:
        if a_sum + b_sum <= limit:
            answer += 1

print(answer)

# =================================================================
# 2 1
# 1 1

# 3