# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

# 나의 정답
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
operations = list(map(list, set(permutations(['add']*op[0] + ['min']*op[1] + ['mul']*op[2] + ['div']*op[3]))))
calculated = []

def use_operation(cur, num, op):
    if op == 'add':
        return cur + num
    elif op == 'min':
        return cur - num
    elif op == 'mul':
        return cur * num
    else:
        if cur >= 0:
            return cur // num
        else:
            return (-cur // num) * -1

for oper_set in operations:
    cur = nums[0]
    for idx in range(len(oper_set)):
        cur = use_operation(cur, nums[idx+1], oper_set[idx])
    calculated.append(cur)

print(max(calculated))
print(min(calculated))

# =================================================================
# 3
# 3 4 5
# 1 0 1 0

# 35
# 17
# =================================================================
# 6
# 1 2 3 4 5 6
# 2 1 1 1

# 54
# -24
# =================================================================