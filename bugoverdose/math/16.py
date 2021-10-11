# Summer/Winter Coding(~2018)
# 소수 만들기
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 

from itertools import combinations 

def solution(nums):
    max_sum = sum(nums)+1
    is_prime = [True]*max_sum
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, max_sum):
        if is_prime[i]:
            for j in range(2*i, max_sum, i):
                is_prime[j] = False
    
    comb = combinations(nums, 3)
    
    answer = 0
    for c in comb:
        if is_prime[sum(c)]:
            answer += 1
    
    return answer

# =================================================================