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
import math 

def solution(numbers):
    answer = 0
    combinations = []
    possible_nums = []

    for i in range(len(numbers)):
        combinations += list(permutations(map(int, list(numbers)), i + 1))

    for combination in combinations:
        num = int(''.join(map(str, combination)))
        if (num not in possible_nums):
            possible_nums.append(num)

    for num in possible_nums:
        if num < 2:
            is_prime = False
        elif num == 2 or num == 3:
            is_prime = True
        else:
            is_prime = True
            for divider in range(2, math.ceil(math.sqrt(num)) + 1):
                if num % divider == 0:
                    is_prime = False
                    break
        if is_prime == True:
            answer += 1

    return answer

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

# 나의 오답 : 시간초과 - 모든 소수들 찾은 후에 만들 수 있는 소수들 탐색하면 너무 느림
def solution(numbers):
    answer = 0
    primes = [2]
    biggest_num = int(''.join(sorted(list(numbers),reverse=True)))
    
    # find all the primes until biggest_num
    for num in range(3, biggest_num + 1):
        is_prime = True
        for divider in range(2, num - 1):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(num)
    
    # find primes that can be made with numbers
    for prime in primes:
        can_be_made = True
        prime_letters = list(str(prime))
        input_letters = list(numbers)
        while (len(prime_letters) > 0):
            if prime_letters[0] not in input_letters:
                can_be_made = False
                break
            input_letters.remove(prime_letters[0])
            prime_letters.remove(prime_letters[0])

            
        if can_be_made == True:
            answer += 1
            
    return answer