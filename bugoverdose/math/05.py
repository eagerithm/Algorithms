# https://www.acmicpc.net/problem/1929
# 숫자 목록에서 소수 여부를 판별하여 출력. 개별적으로 판단시 시간 초과.

# 나의 정답 - 소수 리스트를 만들고 각 입력값에 대해 대조. 시간복잡도 자체는 내려감. O(n^2)=> O(n)
A, B = map(int, input().split())

prime_nums = [False, False] + [True]*B # 각 index에 해당되는 수가 소수인지 대조하여 판별하는 용도

for num in range(2, B+1):
    if prime_nums[num] == True: # 소수의 배수는 전부 소수가 아니게 됨
        for i in range(2 * num, B+1, num):
            prime_nums[i] = False

for num in range(A, B+1):    
    if prime_nums[num]:
        print(num)

# =========================================
# 시간 초과 답 - 입력 값에 대해 개별적으로 판단
A, B = map(int, input().split())

for num in range(A, B+1):
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num) 

# =========================================