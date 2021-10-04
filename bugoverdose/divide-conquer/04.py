# 곱셈 (https://www.acmicpc.net/problem/1629)
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
# 10^10 = 10^5 * 10^5 
# 10^5 = 10^2 * 10^2 * 10^1 
# 10^2 = 10^1 * 10^1  

# n == 짝수
# a^n = a^(n/2) * a^(n/2)
# n == 홀수
# a^n = a^(n/2) a^(n/2) a

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def divide_power(a, b, c):
    if b == 1:
        return a % c
    if b%2 == 0: 
        return divide_power(a, b//2, c) ** 2 % c
    else:
        return (divide_power(a, b//2, c) ** 2) * a % c

print(divide_power(A, B, C))

# ==================================================================
# 10 11 12
# 4