# https://www.acmicpc.net/problem/1978
# 입력된 각 숫자가 소수인지 판별. 소수가 몇개인지 출력.

# 나의 정답 - O(n^2) - 개별적으로 처음부터 판단하므로 느림
input()
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if num == 1:        
        continue 
    is_prime = True
    for div in range(2, num):
        if num % div == 0:
            is_prime = False
            break
    if is_prime == True:
        count += 1
print(count)

# =========================================
# 다른 사람의 풀이 
n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)

# =========================================