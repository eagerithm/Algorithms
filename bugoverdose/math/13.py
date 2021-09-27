# 검문 (https://www.acmicpc.net/problem/2981)

# X0 = a * gcd
# X1 = b * gcd
# 따라서 X1-X0 = (b-a)*gcd 가 되고, 이것은 (X1 - X0)가 gcd의 배수임을 의미한다.

# N1 = a*D + R
# N2 = b*D + R      => N2-N1 = (b-a)*gcd = gcd1
# N3 = c*D + R      => N3-N2 = (c-b)*gcd = gcd2
# 나누는 약수(D)에 따라 R은 변하지만 일관되게 변화하므로 신경쓸 필요가 없어짐
# 짝지어서 gcd들의 gcd를 구하고, 그 약수들을 찾기

# 나의 정답
import sys
import math # math.gcd(A,B)로 A와 B의 최대공약수 찾기 가능

input = sys.stdin.readline

nums = []
gcd = 1
answers = []
length = int(input())

for _ in range(length):
    nums.append(int(input()))

for idx in range(1, length):
    if idx == 1:
        gcd = abs(nums[idx-1] - nums[idx])
    gcd = math.gcd(abs(nums[idx-1] - nums[idx]), gcd)

for div in range(2, round(gcd**0.5)+1): # 제곱근을 중심으로 좌우대칭되므로 절반만 순회
    if gcd%div == 0:
        answers.append(div)
        answers.append(gcd//div)

if gcd not in answers:
    answers.append(gcd)

print(' '.join(map(str, sorted(set(answers))))) # 제곱근이 두개인 경우 때문에 set으로 중복제거

# =================================================================
# 시간초과
import sys

input = sys.stdin.readline

nums = []

for _ in range(int(input())):
    nums.append(int(input()))

nums.sort()
answers = []

for div in range(2, nums[1]-nums[0]+1):
    remainder = nums[0]%div
    if remainder != nums[1]%div: continue

    same_remainders = True

    for num in nums[2:]:
        if remainder != num%div:
            same_remainders = False
            break
    if same_remainders:
        answers.append(div)

print(' '.join(map(str, answers)))

# =================================================================