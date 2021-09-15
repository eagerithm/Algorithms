# 문제 설명
# 출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
# 예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

# 제거한 바위의 위치	각 바위 사이의 거리	    거리의 최솟값
# [21, 17]          	[2, 9, 3, 11]	            2
# [2, 21]	            [11, 3, 3, 8]	            3
# [2, 11]	            [14, 3, 4, 4]       	    3
# [11, 21]	            [2, 12, 3, 8]	            2
# [2, 14]	            [11, 6, 4, 4]	            4
# 위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

# 출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
# 바위는 1개 이상 50,000개 이하가 있습니다.
# n 은 1 이상 바위의 개수 이하입니다.

# 입출력 예
# distance	rocks	            n	return
# 25	    [2, 14, 11, 21, 17]	2	4

# 나의 정답
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    points = [0] + rocks + [distance]
    distances = []
    
    for i in range(1, len(points)):
        distances.append(points[i] - points[i - 1])
    
    min_val = min(distances)
    max_val = distance
    
    while min_val <= max_val:
        mid = int((min_val + max_val)/2)
        to_break = 0
        prev_d = 0
        
        for d in distances:
            if d + prev_d >= mid:
                prev_d = 0
            else:
                prev_d += d
                to_break += 1
                
        print([to_break, min_val, mid, max_val])
        
        if to_break > n: # 너무 많이 부순건 기대하는 최소값이 너무 낮아서       
            max_val = mid - 1
        else:
            answer = mid
            min_val = mid + 1
    
    return answer

# =================================================================
# 다른 사람의 풀이
def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)
    left = 0
    right = distance
    while (left <= right):
        mid = int((left + right) / 2)
        cnt = 0
        p = 0
        for i in range(len(sorted_rocks)):
            if (sorted_rocks[i] - p < mid):
                cnt += 1
            else:
                p = sorted_rocks[i]
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer

# =================================================================
# 틀린 풀이 - 16, [4, 8, 11], 2 => 거리들: [4, 4, 3, 5] => 결과 [11, 5] vs 기대 [8, 8] => 결과 5 < 기대 8
def solution(distance, rocks, n): # 가장 작은 값을 찾으면서 제거하는 greedy 방식
    rocks.sort()
    
    points = [0] + rocks + [distance]
    distances = []
    
    for i in range(1, len(points)):
        distances.append(points[i] - points[i - 1])
    
    for i in range(n):
        min_val = min(distances)
        min_idx = distances.index(min_val)
        
        if min_idx == 0:
            distances.pop(0)
            distances[0] += min_val
        elif min_idx == len(distances) - 1:
            distances.pop()
            distances[-1] += min_val
        else:
            distances.pop(min_idx)
            
            if distances[min_idx - 1] > distances[min_idx]:
                distances[min_idx] += min_val
            else:
                distances[min_idx - 1] += min_val
    
    return min(distances)

# =================================================================