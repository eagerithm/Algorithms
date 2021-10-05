# 숫자 카드 2 (https://www.acmicpc.net/problem/10816)
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

# M의 각 값에 대해서만 이진검색 실행도 가능

# 나의 정답 - 해쉬
N = int(input())
original = list(map(int, input().split()))
original.sort()

dic = {}
for num in original: # 단점: 무조건 모든 데이터를 다 순회해야 함.
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if t not in dic:
        print(0, end = " ")
    else:
        print(dic[t], end = " ")

# ==================================================================