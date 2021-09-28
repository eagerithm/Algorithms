# 스택 수열 (https://www.acmicpc.net/problem/1874)
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
# push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

# 나의 정답 
import sys

input = sys.stdin.readline

N = int(input())

stack = []
target = []
answer = []

for _ in range(N):
    target.append(int(input()))

for num in range(1, N+1):
    while stack:
        if stack[-1] == target[0]:
            stack.pop()
            target.pop(0)
            answer.append('-')
        else:
            break
    if len(stack) == 0 or stack[-1] != target[0]:
        stack.append(num)
        answer.append('+')

if stack[::-1] == target:
    for a in answer:
        print(a)
    for _ in range(len(stack)): # 들어있는 값들 전부 pop
        print('-')
else:
    print("NO")

# ==========================================================
import sys

input = sys.stdin.read

def sol1874():
    n, *nums = map(int, input().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        if st[-1] != num:
            answer = ['NO']
            break
        st.pop()
        answer.append('-')
    print('\n'.join(answer))
   

if __name__ == '__main__':
    sol1874()

# ==========================================================