# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# 입출력 예
# numbers	return
# "17"      3
# "011"     2

# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
# 11과 011은 같은 숫자로 취급합니다.

# 나의 정답
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    
    possible_nums = []
    for num in numbers:
        possible_nums.append(int(num)) # 문자열 값들이라 int 변환 필요
        
    for length in range(2, len(numbers)+1):
        for per in permutations(numbers, length):
            possible_nums.append(int("".join(per))) # 문자열들 합치고 int 변환하여 넣기
    
    possible_nums = sorted(list(set(possible_nums)))
    max_num = max(possible_nums)
    
    is_prime = [True]*(max_num+1)
    is_prime[0] = False
    is_prime[1] = False
    for num in range(2, max_num+1):
        if is_prime[num]:
            for next in range(2*num, max_num+1, num):
                is_prime[next] = False
                
    counter = 0
    for possible_num in possible_nums:
        if is_prime[possible_num]:
            counter+= 1
            
    return counter

# =============================================================
# 다른 사람의 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

# =============================================================
