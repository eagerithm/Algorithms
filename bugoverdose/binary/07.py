# k번째 수 (https://www.acmicpc.net/problem/1300)

# 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. 
# B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 배열 A와 B의 인덱스는 1부터 시작한다. => 구구단 느낌의 데이터

# 나의 정답
N = int(input())
k = int(input())

max_num = k # k번째 수는 k이하의 값
mid = (k+1+1)//2
min_num = 1

while min_num <= max_num:
    num_count = 0
    for i in range(1, N+1): 
        num = mid // i # 각 줄별로 mid 이하의 값들의 개수
        if num > N:
            num = N
        num_count += num
    if num_count >= k:
        max_num = mid - 1
    else:
        min_num = mid + 1
    mid = (max_num+min_num+1)//2

print(mid)

# ==================================================================
# 3
# 7

# 6

# A = [[1 2 3]          # 1의 배수 - 7이하는 7//1 => 3개
#      [2 4 6]          # 2의 배수 - 7이하는 7//2 => 3개
#      [3 6 9]]         # 3의 배수 - 7이하는 7//3 => 2개
# B = [1 2 3 3 4 6 6 9]

# ==================================================================