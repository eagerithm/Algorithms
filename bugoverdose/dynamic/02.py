# 정수 삼각형
# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# 나의 정답
def solution(triangle):
    answer = 0
    
    all_sums = [triangle[0][0]]
    
    for i in range(1, len(triangle)):
        new_sums = []
        for idx in range(len(all_sums)):
            prev_sum = all_sums[idx]
            l = prev_sum + triangle[i][idx]
            r = prev_sum + triangle[i][idx + 1]
            
            if len(new_sums) == 0:
                new_sums.append(l)
                new_sums.append(r)
            elif len(new_sums) < len(all_sums):
                new_sums[idx] = max(new_sums[idx], l)
                new_sums.append(r)
            else:
                new_sums[idx] = max(new_sums[idx], l)
                new_sums.append(r)
            # print(new_sums)
        all_sums = new_sums
            
    return max(all_sums)


# =================================================================
# 다른 사람의 풀이 
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

# =================================================================
# 다른 사람의 풀이 
def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])

# =================================================================
