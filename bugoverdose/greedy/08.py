# 잃어버린 괄호 (https://www.acmicpc.net/problem/1541)
# 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
# 덧셈들에만 전부 괄호를 친다고 간주하면 최초로 -가 나온 이후의 모든 값들은 결국엔 뺄셈에만 사용됨
# 55-50+40
# 55-(50+40) = -35

# 나의 정답
exp = input()

answer = 0
curs = []
substracting = False

for idx in range(len(exp)):
    cur = exp[idx]
    if cur != "+" and cur != "-":
        curs.append(cur)
    elif substracting:
        answer -= int(''.join(curs))
        curs = []
    else:
        answer += int(''.join(curs))
        curs = []
        if cur == "-":
            substracting = True

if substracting:
    answer -= int(''.join(curs))
else:
    answer += int(''.join(curs))

print(answer)

# =================================================================
# 다른 사람의 풀이
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e[0]-sum(e[1:]))

# =================================================================