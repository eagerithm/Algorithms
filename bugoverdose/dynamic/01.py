# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# 입출력 예
# N	number	return
# 5	12	4
# 2	11	3
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.

# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

# 나의 정답
def solution(N, number):
    dic = {}    
    ones = 0
    for i in range(1, 9):
        ones += N * (10 ** (i - 1))
        dic[i] = [ones] # N, NN, NNN, NNNN, ...
    
    for i in range(1, 9):
        for j in range(1, i):
            for each_l in dic[i-j]:
                for each_r in dic[j]:  
                    dic[i].append(each_l + each_r)
                    dic[i].append(each_l - each_r)
                    dic[i].append(each_l * each_r)
                    if each_r != 0:
                        dic[i].append(each_l // each_r)
                        
        if number in dic[i]:
            return i

    return -1

# =================================================================
# 다른 사람의 풀이 
def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)): # 절반까지만 순회하고, 각 케이스에 대해 앞뒤 변경하며 추가.
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y) # 곱셈은 한번만 해도 됨.
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1
    
# =================================================================
