# 팩토리얼 : N!을 출력하는 프로그램

# 나의 정답
N = int(input())

def multiply(i, n):
    if n != 1:
        i *= n
        n -= 1
        return multiply(i, n)
    else:
        return i

if N <= 1:
    print(1)
else:
    print(multiply(1, N))

# =========================================
# 다른 사람의 풀이 - 세련된 재귀
def recur(x):
    if x < 2: 
        return 1
    return x*recur(x-1)
print(recur(int(input())))

# =========================================
# 다른 사람의 풀이 - 반복문
d=1
for i in range(1,int(input())):
    d*=i+1
print(d)

# =========================================