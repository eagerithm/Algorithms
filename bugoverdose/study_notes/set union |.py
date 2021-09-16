# greedy/05.py
a_set = set() # 비어있는 집합으로 초기화
b_set = set()

a_set = {1, 2, 3}
b_set = {4}
c_set = {5}
d_set = set()

# union() : 특정 set에 다른 set들을 합친 결과를 반환
print(a_set.union(b_set, c_set, d_set)) # {1, 2, 3, 4, 5}

# | : 합집합 연산 간편법
print(a_set|b_set|c_set|d_set)          # {1, 2, 3, 4, 5}
