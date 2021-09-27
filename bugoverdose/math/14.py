# 조합 0의 개수 (https://www.acmicpc.net/problem/2004)

# N!까지의 곱 중 2가 몇승인지만 효율적으로 체크하는 방법
# while max>1:
#     max = max//2 # 2의 배수들, 4의 배수들, 8의 배수들을 순차적으로 전부 1번씩 카운트
#     twos += max

# 나의 정답
N, M = map(int, input().split()) # 0 <= M <= N <= 2000000000

def two_fives(n): 
    twos = 0
    fives = 0

    max = n
    while max>1:
        max = max//2 # 2의 배수들, 4의 배수들, 8의 배수들을 순차적으로 전부 1번씩 카운트
        twos += max

    max = n
    while max>1:
        max = max//5 
        fives += max

    return twos, fives

two_count, five_count = two_fives(N) # N!

two, five = two_fives(M) # // r!
two_count -= two
five_count -= five

two, five = two_fives(N-M) # // (n-r)!
two_count -= two
five_count -= five

print(max(0, min(two_count, five_count)))

# =================================================================
# 시간초과 - 직접 하나씩 나누는 방법
N, M = map(int, input().split()) # 0 <= M <= N <= 2000000000

def two_fives(n): 
    twos = 0
    fives = 0

    while n%2 == 0:
        n = n//2
        twos += 1

    while n%5 == 0:
        n = n//5
        fives += 1

    return twos, fives

two_count = 0
five_count = 0

for num in range(N, min(M, N-M), -1):
    two, five = two_fives(num)
    two_count += two
    five_count += five

if M >= 2:
    for num in range(2, M+1):
        two, five = two_fives(num)
        two_count -= two
        five_count -= five

print(max(0, min(two_count, five_count)))

# =================================================================