# 소수의 연속합 (https://www.acmicpc.net/problem/1644)
# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.

# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)

# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

# 에라토스테네스의 체 - 한번 체크한 수의 배수들을 검사 대상에서 제외시키는 방식으로 소수 수열 구하는 기법

# 나의 정답
N = int(input())

def solution(N):
    if N == 1: return 0

    # 에라토스테네스의 체
    is_prime = [True]*(N+1)
    primes = []
    for num in range(2, N+1):
        if is_prime[num]:
            primes.append(num)
            for n in range(num, N+1, num):
                is_prime[n] = False

    prime_sum_num = 0

    left = 0 # idx 기준
    right = 0
    cur_sum = primes[0]
    max_index = len(primes)

    while right <= max_index-1:
        if cur_sum <= N:
            if cur_sum == N:
                prime_sum_num += 1
            right += 1
            if right >= max_index: break
            cur_sum += primes[right]
        else: # cur_sum > N:
            cur_sum -= primes[left]
            left += 1

    return prime_sum_num

print(solution(N))

# =================================================================
