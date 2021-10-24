# LCS 2 (https://www.acmicpc.net/problem/9252)
# LCS(Longest Common Subsequence, 최장 공통 부분 수열) 문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

A = [""] + list(input())
B = [""] + list(input())

lcs = [[""]*len(A) for _ in range(len(B))]

for b_idx in range(1, len(B)):
    for a_idx in range(1, len(A)):
        if A[a_idx] == B[b_idx]:
            lcs[b_idx][a_idx] = lcs[b_idx-1][a_idx-1] + str(A[a_idx])
        else:
            if len(lcs[b_idx-1][a_idx]) < len(lcs[b_idx][a_idx-1]):
                lcs[b_idx][a_idx] = lcs[b_idx][a_idx-1]
            else:
                lcs[b_idx][a_idx] = lcs[b_idx-1][a_idx]

print(len(lcs[-1][-1]))
print(lcs[-1][-1])

#  =================================================================