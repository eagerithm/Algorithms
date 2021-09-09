# list.pop(index) : index번째 데이터를 리스트에서 제거하면서 반환
# 스택 구조로 간주

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0)) # 0

print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(3)) # 4

print(l) # [1, 2, 3, 5, 6, 7, 8, 9]

# ============================
data = ["infy", "tcs", "affle", "dixon", "astral"] 

last_element = data.pop() # 디폴트로 마지막 요소 제거하면서 반환 
print(last_element) # astral

# =========================================================
# list.remove(value) : value에 해당하는 값을 리스터 처음부터 찾고 하나를 제거

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Bob')
print(l)
# ['Charlie', 'Bob', 'Dave']

# =========================================================