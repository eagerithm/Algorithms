# 괄호의 값 (https://www.acmicpc.net/problem/5430)
# (()[[]])([])의 괄호값 : (()[[]]) => 2×11=22 / ([]) => 2×3=6 / 전체 괄호열의 값은 22 + 6 = 28

# 스택에 "("와 "["도 넣고, 그로 인한 현재 점수들도 넣어서 적절하게 둘 다 활용 
stack = []
valid = True

for x in list(input().strip()):
    print(stack)
    if not valid: break

    val = 0
    if x == ")":
        if len(stack) == 0 or stack[-1] == "[":
            valid = False
            break
        while len(stack) != 0:
            print(stack)
            cur = stack.pop()
            if cur == "(":
                if val == 0:
                    stack.append(2)
                else:
                    stack.append(2*val)
                break
            elif cur == "[":
                valid = False
                break
            else:
                val += cur # (()[[]]) => (2 => (2[[ => (2[3 => (2+9 => 22

    elif x == "]":
        if len(stack) == 0 or stack[-1] == "(":
            valid = False
            break
        while len(stack) != 0:
            print(stack)
            cur = stack.pop()
            if cur == "[":
                if val == 0:
                    stack.append(3)
                else:
                    stack.append(3*val)
                break
            elif cur == "(":
                valid = False
                break
            else:
                val += cur
    
    else:
        stack.append(x)
    
print(stack)
if "(" in stack or "[" in stack:
    valid = False

if valid:
    print(sum(stack))
else:
    print(0)
    
# ==========================================================
# (()[[]])([])
# 28

# 스택 변화 과정
# []
# ['(']
# ['(', '(']
# ['(', 2]
# ['(', 2, '[']
# ['(', 2, '[', '[']
# ['(', 2, '[', 3]
# ['(', 2, '[']
# ['(', 2, 9]
# ['(', 2]
# ['(']
# [22]
# [22, '(']
# [22, '(', '[']
# [22, '(', 3]
# [22, '(']
# [22, 6]