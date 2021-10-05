# 수 찾기 (https://www.acmicpc.net/problem/1920)
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = list(map(int, input().split()))

center = N//2 # 홀수면 정중앙, 짝수면 중앙에서 오른쪽 index

for target in targets:
    exists = 0 # 존재하면 1을, 존재하지 않으면 0을 출력
    mid = center # idx의 위치들을 조정
    left = 0
    right = N-1
    while left <= right:
        if nums[mid] == target: # 어떤 idx를 수정할지를 판단하기 위해서만 실제 값을 사용
            exists = 1
            break
        elif target < nums[mid]:
            right = mid - 1
        elif nums[mid] < target: # 12345에서 5를 찾는데 현재 3을 조회한 경우 45로 옮겨야 함
            left = mid + 1
        mid = (left+right+1)//2
    print(exists)

# ==================================================================