# 가장 긴 증가하는 부분 수열 4 (https://www.acmicpc.net/problem/14002)

input()
seq = list(map(int, input().split()))

dp = [0]
sub_seq = {}
sub_seq[0] = [0]

for s in seq:
    if dp[-1] < s:
        length = len(dp)
        dp.append(s)
        sub_seq[length] = sub_seq[length-1] + [s]
    else:
        left = 0
        right = len(dp)-2
        max_mid = 0
        while left <= right:
            mid = (left+right)//2
            if dp[mid] < s:
                max_mid = mid
                left = mid+1
            else:
                right = mid-1
        sub_seq[max_mid+1] = sub_seq[max_mid] + [s]
        dp[max_mid+1] = s

length = len(dp)-1

print(length)
print(" ".join(map(str, sub_seq[length][1:])))

# =================================================================
# 10
# 9 20 7 30 19 50 10 20 30 40

# 5
# 7 10 20 30 40