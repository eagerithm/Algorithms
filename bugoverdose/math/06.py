# https://www.acmicpc.net/problem/9020
# 골드바흐의 추측
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다

# 나의 정답
import sys

input = sys.stdin.readline

inputs = []

for _ in range(int(input())):
    inputs.append(int(input()))

max_input = max(inputs)

primes = [False, False] + [True] * max_input

for i in range(2, max_input):
    if primes[i]:
        for j in range(i+i, max_input, i):
            primes[j] = False

for n in inputs:
    a, b = 0, 0 
    for i in range(2, n//2+1):
        if primes[i] and primes[n-i]:
            a, b = i, n-i 
    print(a, b)

# =========================================