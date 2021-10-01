# 트리 순회 (https://www.acmicpc.net/problem/1991)
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

import sys

input = sys.stdin.readline

node = {}

for _ in range(int(input())):
    cur, left, right = input().split()
    node[cur] =[left, right]

preorder = []  # 루트-왼-오
inorder = []   # 왼-루트-오
postorder = [] # 왼-오-루트

def preorder_dfs(stack, preorder):
    cur = stack.pop()
    cur_left = node[cur][0]
    cur_right = node[cur][1]
    preorder.append(cur)
    if cur_left != ".":
        stack.append(cur_left)
        stack, preorder = preorder_dfs(stack, preorder)
    if cur_right != ".":
        stack.append(cur_right)
        stack, preorder = preorder_dfs(stack, preorder)
    return stack, preorder

def inorder_dfs(stack, inorder):
    cur = stack.pop()
    cur_left = node[cur][0]
    cur_right = node[cur][1]
    if cur_left != ".":
        stack.append(cur_left)
        stack, inorder = inorder_dfs(stack, inorder)
    inorder.append(cur)
    if cur_right != ".":
        stack.append(cur_right)
        stack, inorder = inorder_dfs(stack, inorder)
    return stack, inorder

def postorder_dfs(stack, postorder):
    cur = stack.pop()
    cur_left = node[cur][0]
    cur_right = node[cur][1]
    if cur_left != ".":
        stack.append(cur_left)
        stack, postorder = postorder_dfs(stack, postorder)
    if cur_right != ".":
        stack.append(cur_right)
        stack, postorder = postorder_dfs(stack, postorder)
    postorder.append(cur)
    return stack, postorder

_, preorder = preorder_dfs(["A"], preorder)
print(''.join(preorder))

_, inorder = inorder_dfs(["A"], inorder)
print(''.join(inorder))

_, postorder = postorder_dfs(["A"], postorder)
print(''.join(postorder))

# ==============================================================
