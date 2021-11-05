# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# 입출력 예
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5

# 나의 정답 - BFS : (numbers의 길이 == 최대 level == n일 때) 2의 n승가지의 경우의 수 모두 계산 후 순회
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)])

    while (queue):
        cur_sum, level = queue.popleft()

        if level == len(numbers) and target == cur_sum:
            answer += 1
        if level < len(numbers):
            queue.append((cur_sum + numbers[level], level + 1))
            queue.append((cur_sum - numbers[level], level + 1))

    return answer

# =================================================================
# 나의 정답2
from collections import deque

def solution(numbers, target):
    answer = 0
    f = numbers[0]
    length = len(numbers) 

    queue = deque([(f, 0), (-f, 0)])
    while queue:
        cur, cur_idx = queue.popleft()
        cur_idx += 1
        if cur_idx == length:
            if cur == target:
                answer += 1
            continue
        
        queue.append((cur+numbers[cur_idx], cur_idx))
        queue.append((cur-numbers[cur_idx], cur_idx))
        
    return answer

# =================================================================
# 다른 사람의 풀이 - 재귀함수 극한 버전
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# =================================================================
# 다른 사람의 풀이 - DFS
def solution(numbers, target):
    result = 0

    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)
    return result

# =================================================================
