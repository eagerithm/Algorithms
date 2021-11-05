# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# 입출력 예
# prices            return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

# 나의 정답 - 데큐를 통한 성능 개선
from collections import deque

def solution(prices):
    answers = [0]*len(prices)
    prices = deque(prices)
    cur_time = 0
    stack = deque([(prices.popleft(), cur_time)])
    
    while prices:
        cur_time += 1
        while stack:
            if stack[-1][0] <= prices[0]: break
            _, prev_time = stack.pop()
            answers[prev_time] = cur_time-prev_time
        stack.append((prices.popleft(), cur_time))
                
    while stack:
        _, prev_time = stack.popleft()
        answers[prev_time] = cur_time-prev_time
        
    return answers

# ==========================================================
# 나의 정답 - 스택
def solution(prices):
    answer = [0] * len(prices)   
    stack = []
    
    for index in range(len(prices)):
        while stack and stack[-1][1] > prices[index]: # 하락하면 종료
            start, price = stack.pop()
            answer[start] = index - start
        stack.append([index, prices[index]])

    # 끝까지 하락하지 않은 경우 전체 거리 할당
    for start, price in stack:
        if answer[start] == 0:
            answer[start] = len(prices) - start - 1
                
    return answer

# ==========================================================
# 다른 사람의 풀이 - 스택
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = list()
    stack.append((0, prices[0]))

    for index in range(1, len(prices)):
        while stack and stack[-1][1] > prices[index]:
            (prev, value) = stack.pop()
            answer[prev] = (index - prev)
        stack.append((index, prices[index]))

    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(prices) - i - 1
    return answer

# ==========================================================
# 다른 사람의 풀이 - 큐
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

# ==========================================================