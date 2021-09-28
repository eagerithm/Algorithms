# 오큰수 (https://www.acmicpc.net/problem/17298)
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

# 나의 정답 
N = int(input())
nums = list(map(int, input().split()))

stack = []
answer = []

for idx in range(N):
    if len(stack) == 0:
        stack.append((idx, nums[idx]))
        continue

    while stack:
        if stack[-1][1] < nums[idx]:
            answer.append((stack.pop()[0], nums[idx]))
        else:
            break

    stack.append((idx, nums[idx]))

for s in stack:
    answer.append((s[0], -1))

print(' '.join(map(lambda x:str(x[1]), sorted(answer, key=lambda x:x[0]))))

# ==========================================================
# 다른 사람의 풀이 - 끝부터 순회하는 최초 접근법 개선버전
n = int(input())
a = list(map(int, input().split()))
out = [0 for _ in range(n)] # 미리 생성해놓으면 더 효율적
stack = []

idx = n-1
while a :
	x = a.pop()
	while stack :
		if stack[-1] <= x : # 스택에서 현재 값보다 작거나 같은 값들 전부 제거
			stack.pop()
		else :
			break
	if stack : # 스택에 남은 값들은 전부 자신보다 큼
		out[idx] = stack[-1] # 스택에 남은 값 중 가장 마지막에 추가된 값이 오큰수. 나머지 확인할 필요 없음.
	else :
		out[idx] = -1
	stack.append(x)
	idx -= 1
print(' '.join(map(str, out)))

# ==========================================================
# 시간 초과 - 불필요한 가정과 과정. 시간복잡도 높음
N = int(input())
nums = list(map(int, input().split()))

stack = [nums.pop()]
answer = [-1]
max_num = stack[0] # stack에 존재하는 최대값. 오큰수 존재 여부 사전 확인 => 성능개선?

for _ in range(N-1):
    cur = nums.pop() # 오른쪽 끝부터 하나씩 
    nge = -1 # 오큰수가 없으면 -1

    while stack:
        if stack[-1] < cur: # 스택에서 현재 값보다 작은 값들 전부 제거하고 본인 추가
            stack.pop()
        else:
            break

    if max_num < cur: # 스택의 최대값보다 현재값이 크면 오큰수 없음 + 스택에 추가할 예정인 현재값을 최대값으로 갱신
        max_num = cur
    else:
        for big in stack[::-1]: # 스택 가장 바닥부터 오큰수 찾기 # 이 작업 불필요!!! # 가장 최신에 추가된 값만 필요
            if cur < big:
                nge = big
                break
    
    stack.append(cur)
    answer.append(nge)
    
print(' '.join(map(str, answer[::-1])))

# ==========================================================