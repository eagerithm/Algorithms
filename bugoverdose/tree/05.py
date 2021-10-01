# 이진 검색 트리 (https://www.acmicpc.net/problem/5639)
# 이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.
# 1 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 2 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# 3 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

# 전위순회한 결과를 받아 후위순회한 결과를 출력하기

# ==============================================================
# 전위순회 결과는 [ 부모 | left | right ]로 구분 가능
# 50 30 24 5 28 45 98 52 60
# 50 | 30 24 5 28 45 | 98 52 60  ==> 50-30-98이 루트-왼-오
# 30 | 24 5 28 | 45
# 24 | 5 | 28
# 98 | 52 60 | 
# 52 |  | 60 

# 나의 정답2 - 정규화된 풀이방식
# 전위순회한 결과를 받아 후위순회한 결과를 출력
import sys
from collections import deque
sys.setrecursionlimit(10000)

node = {}
preorder = deque() # 루트-왼-오
postorder = [] # 왼-오-루트

for line in sys.stdin:
    preorder.append(int(line))

root = [preorder[0]]

for idx in range(len(preorder)):
    node[preorder[idx]] = [-1,-1]

# 전위순회 결과로 노드 간의 관계 확인 : [ 부모 | left | right ]
def dfs_preorder(preorder):
    root = preorder.popleft()
    left = deque()
    for cur in list(preorder):
        if cur < root:
            left.append(preorder.popleft())
    right = preorder

    if len(left) >= 1:
        node[root][0] = left[0]
        if len(left) >= 2:
            dfs_preorder(left)

    if len(right) >= 1:
        node[root][1] = right[0]
        if len(right) >= 2:
            dfs_preorder(right)

dfs_preorder(preorder)

# 노드 간의 관계에 따라 후위순회
def postorder_dfs(stack, postorder):
    cur = stack.pop()
    if node[cur][0] != -1:
        stack.append(node[cur][0])
        stack, postorder = postorder_dfs(stack, postorder)
    if node[cur][1] != -1:
        stack.append(node[cur][1])
        stack, postorder = postorder_dfs(stack, postorder)
    stack.append(cur)
    postorder.append(cur)
    return stack, postorder

_, postorder = postorder_dfs(root, postorder)

for n in postorder:
    print(n)

# ==============================================================
# 나의 정답1 - 메모리와 성능 더 나은 방법
import sys
sys.setrecursionlimit(10000)

node = {}
preorder = [] # 루트-왼-오
postorder = [] # 왼-오-루트

for line in sys.stdin:
    preorder.append(int(line))

for idx in range(len(preorder)):
    node[preorder[idx]] = [-1,-1]

stack = []

# 전위순회 결과로 노드 간의 관계 확인
for cur in preorder: 
    if len(stack) == 0:
        stack.append(cur)
        continue
    if cur < stack[-1]:
        node[stack[-1]][0] = cur # 루트의 왼쪽 자녀로 배정
        stack.append(cur)
        continue

    # 바로 이전 노드보다 큰 경우 누구의 오른쪽 자녀인지 최상위루트부터 체크 
    idx = -1
    for p_idx in range(len(list(stack))):
        prev = stack[p_idx]
        if prev < cur:
            node[prev][1] = cur
            idx = p_idx # 현재 오른쪽 자식을 추가한 부모노드 
            break
    stack = stack[:idx]
    stack.append(cur)

# 노드 간의 관계에 따라 후위순회
def postorder_dfs(stack, postorder):
    cur = stack.pop()
    if node[cur][0] != -1:
        stack.append(node[cur][0])
        stack, postorder = postorder_dfs(stack, postorder)
    if node[cur][1] != -1:
        stack.append(node[cur][1])
        stack, postorder = postorder_dfs(stack, postorder)
    stack.append(cur)
    postorder.append(cur)
    return stack, postorder

root = [preorder[0]]
_, postorder = postorder_dfs(root, postorder)

for n in postorder:
    print(n)

# ==============================================================
# 전위 순회 입력
# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60

# 후위 순회 출력
# 5
# 28
# 24
# 45
# 30
# 60
# 52
# 98
# 50