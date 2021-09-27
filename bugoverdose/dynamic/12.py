# 1로 만들기 (https://www.acmicpc.net/problem/1463)
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

N = int(input())

curs = [N]
count = 0 

while True:
    if 1 in curs:
        break
    cur_len = len(curs)
    for idx in range(cur_len):
        if curs[idx]%3 == 0:
             curs.append(curs[idx]//3)
        if curs[idx]%2 == 0:
             curs.append(curs[idx]//2)
        curs[idx] -= 1
    count += 1

print(count)

# =================================================================