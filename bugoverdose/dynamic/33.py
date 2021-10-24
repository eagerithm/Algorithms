# LCS (https://www.acmicpc.net/problem/9251)
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

A = ["NONE"] + list(input())
B = ["NONE"] + list(input())

lcs = [[0]*(len(A)) for _ in range(len(B))]

for b_idx in range(1, len(B)):
    for a_idx in range(1, len(A)):
        if A[a_idx] == B[b_idx]:
            lcs[b_idx][a_idx] = lcs[b_idx-1][a_idx-1] + 1
        else:
            lcs[b_idx][a_idx] = max(lcs[b_idx][a_idx-1], lcs[b_idx-1][a_idx])

print(max(lcs[len(B)-1]))

#  =================================================================