# https://www.acmicpc.net/problem/10870
# 피보나치 수 5

# 나의 정답
N = int(input())

fibonacci = [0, 1]

def fill_fibonacci(target_idx, fibonacci):
    if target_idx >= len(fibonacci):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        return fill_fibonacci(target_idx, fibonacci)
    return fibonacci

print(fill_fibonacci(N, fibonacci)[N])

# =========================================
# 다른 사람의 풀이 - 최종 값만 반환하는 재귀
def r(x):
    if x < 2: 
        return x
    return r(x-1) + r(x-2)
print(r(int(input())))

# =========================================