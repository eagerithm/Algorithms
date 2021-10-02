# 트리의 순회 (https://www.acmicpc.net/problem/2263)
# inorder와 postorder를 받아 preorder를 출력 

#      1 
#  2       3 
# 4 5     6 7 

# 전위 : 1 245 367 
# 중위 : 425 1 637   - [left 부모 right]
# 후위 : 452 673 1   - [left right 부모]

# 후위에서 부모를 찾아 중위를 좌우로 나누는 과정을 반복
# 별도로 전위순회하지 않아도 이 과정에서 부모-left-right 순으로 부모노드들 전부 나열하면 전위순회 결과가 됨

# 정답 - 노드의 위치 정보 저장할 필요도 없음. 중위를 좌우로 나누는 작업에서 부모-좌-우 순으로 자동으로 순회됨
import sys
from collections import deque

sys.setrecursionlimit(40000)

N = int(input())

# preorder = []
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_idx = [0]*(N+1) # 0~N+1까지
for idx in range(N):
    inorder_idx[inorder[idx]] = idx # 특정 값이 inorder의 어디에 있는가 - index 정보만 저장 

def devide(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end: # 잘못된 경우
        return

    root = postorder[post_end]
    root_idx = inorder_idx[root] # 중위순회상에서의 root 위치
    post_end -= 1
    
    left_len = root_idx - in_start
    right_len = in_end - root_idx # 중위순회상 부모노드에 의해 갈리는 좌우의 요소 개수

    print(root, end=" ") # 줄바꿈 없이 한칸씩 띄우며 그대로 출력
    # preorder.append(root) # 출력 과정에서 메모리 초과 가능

    devide(in_start, in_start+left_len-1, post_start, post_start+left_len-1) # left
    devide(in_end-right_len+1, in_end, post_end-right_len+1, post_end) # right
    return 

devide(0, len(inorder)-1, 0, len(postorder)-1)

# print(' '.join(map(str, preorder))) # 배열로 계속 만드는 과정에서 메모리 초과

# ==============================================================
# 메모리 초과
import sys

N = int(input())

node = {}

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

def devide(inorder, postorder):
    root = postorder.pop()
    r_idx = -1
    for idx in range(len(inorder)):
        if inorder[idx] == root:
            r_idx = idx
            break
    if r_idx != -1:
        preorder.append(root)
    
    left = -1
    right = -1
    if 1 <= r_idx:
        left = devide(inorder[:r_idx], postorder[:r_idx])
    if r_idx <= len(inorder)-2:
        right = devide(inorder[r_idx+1:], postorder[r_idx:])
    node[root] = [left, right]
    return root

root = devide(inorder, postorder)

# def preorder_dfs(stack, preorder):
#     root = stack.pop()
#     left = node[root][0]
#     right = node[root][1]

#     preorder.append(root)
#     if left != -1:
#         stack.append(left)
#         stack, preorder = preorder_dfs(stack, preorder)
#     if right != -1:
#         stack.append(right)
#         stack, preorder = preorder_dfs(stack, preorder)

#     return stack, preorder

# _, preorder = preorder_dfs([root], [])

print(' '.join(map(str, preorder)))

# ==============================================================