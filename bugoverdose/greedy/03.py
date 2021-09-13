# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# 입출력 예
# number	    k	return
# "1924"	    2	"94"
# "1231234"	    3	"3234"
# "4177252841"	4	"775841"

# 나의 정답
def solution(number, k):
    number = list(map(int, number))
    answer_len = len(number) - k
    stack = [number[0]]
    
    for num in number[1:]:
        while stack:
            if stack[-1] < num and k > 0:
                stack.pop() # 추가되려는 값이 더 크면 스택의 마지막 값 제거 (981 + 7 => 987)
                k -= 1
            else:
                break
        stack.append(num) # stack에 최대~최소 순으로 값 추가 (98765)
    
    if k > 0:
        stack = stack[:-k] # 제거가 필요하면 맨끝의 가장 작은 값들만 제거
    
    return ''.join(map(str, stack))

# =================================================================
# 다른 사람의 풀이 - 스택에 마지막으로 추가된 값보다 다음에 추가할 값이 더 크면 대체 / 더 작은 값이면 그냥 추가
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k] # 오른쪽 값들 k개 제외
    return ''.join(stack)

# =================================================================
# 느린 풀이1 : 11/12 
def solution(number, k):
    answer_len = len(number) - k
    answer = []
    numbers = list(map(int, number))

    while k > 0:
        if len(numbers) == k + 1:
            answer.append(max(numbers))
            numbers.clear()
            break
            
        left = numbers[:k + 1]
        right = numbers[k + 1:]
        
        max_num = max(left)
        max_idx = left.index(max_num)
        
        if max_idx == 0:
            answer.append(numbers.pop(0))
            continue        
        
        numbers = left[max_idx:] + right
        k -= max_idx
    
    answer += numbers
    
    return ''.join(map(str, answer))
    
# =================================================================
# 느린 풀이2 : 10/12
def solution(number, k):
    numbers = list(number)
    cur = 1
    
    while k > 0 and cur < len(numbers):
        if numbers[cur - 1] < numbers[cur]:
            numbers.pop(cur - 1)
            k -= 1            
            cur = cur - 1 if cur >= 2 else cur
        else:
            cur += 1
    
    return ''.join(numbers)

# =================================================================