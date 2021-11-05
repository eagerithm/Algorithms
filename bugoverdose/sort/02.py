# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 입출력 예
# numbers	             return
# [6, 10, 2]             "6210"
# [3, 30, 34, 5, 9]      "9534330" 
# [2, 21, 22]            "22221"
# [2, 23, 29]            "29232"
# [9, 90, 99, 900, 909]  "99990909900"
# [0, 0, 0, 0]           "0"            # int 변환 작업 필요
# 다른 사람의 풀이1
def solution(numbers):
    numbers = list(map(str, numbers)) # 각 숫자들에 str() 적용하여 문자열로 변환하여 재할당
    numbers.sort(key=lambda x: x*3, reverse=True) # 9 vs 909 => 999 vs 909909909 기준으로 원본 numbers 정렬 (Null 반환)
    return str(int(''.join(numbers))) # 각 문자열들을 합치기. 사이에는 공백 없음('') 

# 다른 사람의 풀이2
def solution(numbers):
    answer = '' 
    
    numbers2 = [str(n)*3 for n in numbers] 
    numbers3 = list(enumerate(numbers2))
    numbers3.sort(key = lambda x:x[1], reverse = True)
    
    for index, value in numbers3:
        answer += str(numbers[index])
        
    return str(int(answer))

# 나의 오답 : [2, 21, 22] => 22212 < 22221
def solution(numbers):
    answer = ''
    
    sorted_num_str = sorted(map(lambda x:str(x), numbers), reverse = True) 
    
    for num in sorted_num_str:
        answer += num
    
    return answer