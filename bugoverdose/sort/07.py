# 좌표 압축 : https://www.acmicpc.net/problem/18870
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 나의 정답
length = int(input())
nums = list(map(int, input().split()))
points = {}
idx = 0
for num in sorted(list(set(nums))):
    points[num] = idx
    idx += 1

smaller_points = []

for num in nums:
    smaller_points.append(points[num])

print(' '.join(map(str, smaller_points)))

# =========================================
# 시간초과 - index()는 찾는 값이 나올 때까지 리스트 전체를 순차적으로 탐색. O(n^2)
length = int(input())
nums = list(map(int, input().split()))
points = sorted(list(set(nums)))

smaller_points = []

for num in nums:
    smaller_points.append(points.index(num))

print(' '.join(map(str, smaller_points)))

# =========================================
# 시간초과
bigger_count = []

length = int(input())

nums = list(map(int, input().split()))

for num in nums:
    bigger_count.append(sum(map(lambda x:num>x, nums)))

print(' '.join(map(str, bigger_count)))

# =========================================
# 5
# 2 4 -10 4 -9

# 2 3 0 3 1