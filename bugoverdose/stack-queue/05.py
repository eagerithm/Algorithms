# 균형잡힌 세상 (https://www.acmicpc.net/problem/4949)
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

# 나의 정답 
import sys

for line in sys.stdin:
    stack = []
    is_vps = True
    string = line.rstrip()

    if string == ".": break

    for p in list(string):
        if p == '(' or p =='[':
            stack.append(p)
        elif p == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                is_vps = False
                break
        elif p == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and len(stack) == 0:
        print("yes")
    else:
        print("no")

# ==========================================================
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

# yes
# yes
# no
# no
# no
# yes
# yes
# ==========================================================