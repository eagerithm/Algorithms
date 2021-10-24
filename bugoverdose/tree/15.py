# 개미굴 (https://www.acmicpc.net/problem/14725)
# 트라이 구조 입문

import sys

input = sys.stdin.readline
routes = {}

for _ in range(int(input())):
    route = list(input().split())
    cur_dic = routes
    for cur in route[1:]:
        if cur not in cur_dic:
            cur_dic[cur] = {}
        cur_dic = cur_dic[cur] # dictionary의 참조값만 할당하므로 계속 이어나갈 수 있음

def print_each(dic, parent, level):
    print("--"*level + parent)
    for child in sorted(dic[parent].keys()):
        print_each(dic[parent], child, level+1)

for root in sorted(routes.keys()):
    print_each(routes, root, 0)

#  =================================================================
# 3
# 2 B A
# 4 A B C D
# 2 A C

# A
# --B
# ----C
# ------D
# --C
# B
# --A
#  ========================
# 4
# 2 KIWI BANANA
# 2 KIWI APPLE
# 2 APPLE APPLE
# 3 APPLE BANANA KIWI

# APPLE
# --APPLE
# --BANANA
# ----KIWI
# KIWI
# --APPLE
# --BANANA
#  =================================================================