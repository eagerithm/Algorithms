# 가장 긴 증가하는 부분 수열 (https://www.acmicpc.net/problem/11053)
# LIS(Longest Increasing Subsequence)
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 나의 정답
int(input())

min_num = 9999

nums = list(map(int, input().split())) # 1~1000의 값들로 구성된 수열

last_vals = [0, nums[0]] # last_vals[i] : 현재 단계까지 길이가 i일 수 있는 부분수열들 중 마지막값의 최소값

for num in nums[1:]:
    max_len = len(last_vals)-1

    if num > last_vals[-1]:
        last_vals.append(num)

    for idx in range(max_len, 0, -1):
        if last_vals[idx-1] < num and num < last_vals[idx]: # 현재값보다 작은 경우 이전단계까지의 부분수열에 붙이기
            last_vals[idx] = num

print(len(last_vals)-1)

# =================================================================
# 다른 사람의 풀이 : 마지막 값이 같으면서 더 짧은 부분수열들은 고려하지 않는 방법
input()
opt = [0]
for x in map(int, input().split()):
    if opt[-1] < x: # 기본적으로 opt[3]은 길이가 3인 부분수열의 마지막 값 중 최소값
        opt.append(x)
    else:
        i = -2 # 마지막 이전 부분수열들 순차적으로 검토
        while x <= opt[i]: 
            i -= 1 
        # opt[i] < x가 되는 최초의 부분수열의 뒤에 현재 값을 이어붙임
        opt[i + 1] = x # 현재값이 붙을 수 있는 가장 긴 부분수열 1개 외에는 굳이 갱신하지 않음

print(len(opt) - 1)
# 6
# 10 20 9 30 19 50

# 4
# =================================================================
# opt의 변화
# 0 10 
# 0 10 20
# 0 9 20  # [9]부터 다시 시작
# 0 9 20 30 
# 0 9 19 30  # [9 19]부터 다시 시작
# 0 9 19 30 50
# 최종적으로 opt[4]가 최대값인 부분수열의 길이가 최대

# =================================================================