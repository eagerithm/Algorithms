# Bigger is Greater (https://www.hackerrank.com/challenges/bigger-is-greater/problem)

# 사전순위상 바로 다음 순서의 문자열
for _ in range(int(input())):
    origin = input().strip()
    idx = len(origin)-1
    found = False
    while idx >= 1:
        if origin[idx-1] < origin[idx]:
            found = True
            break
        idx -= 1
    
    if not found:
        print("no answer")
        continue

    new = origin[:idx-1]
    cur_middle = origin[idx-1]
    right = list(origin[idx:])

    for second_idx in range(1, len(right)+1):
        if cur_middle < right[-second_idx]:
            new += right[-second_idx]
            right[-second_idx] = cur_middle
            break
    new += "".join(sorted(right))

    print(new)

#  =================================================================