# 가장 긴 증가하는 부분 수열 2 (https://www.acmicpc.net/problem/12015)
# dp : O(n^2) - dynamic/14.py 참고 
# binary search : O(n*log n) - 기본 아이디어는 dp와 동일. 부분적으로만 로직 개선.

input()
seq = list(map(int, input().split()))
last_nums = [0] # 모든 부분수열이 {0, ... } 형식이라고 간주

for cur in seq:
    if last_nums[-1] < cur:
        last_nums.append(cur)
    else:
        right = len(last_nums) - 2
        mid = (right+1)//2
        left = 0
        max_smaller = 0
        while left <= right:
            if last_nums[mid] < cur:
                left = mid+1
                max_smaller = max(mid, max_smaller)
            else:
                right = mid-1
            mid = (left+right+1)//2
        last_nums[max_smaller+1] = cur
print(len(last_nums)-1)

# ==================================================================
# 6
# 10 20 9 30 19 50

# 4