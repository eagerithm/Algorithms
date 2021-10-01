from collections import Counter  
 
arr = [1,2] + [3 for _ in range(10)] + [4,5,6,7,7]
val = Counter(arr).most_common()  
print(val)
# [(3, 10), (7, 2), (1, 1), (2, 1), (4, 1), (5, 1), (6, 1)]
# 배열 arr 안에 3이 10회 등장, 7이 2회 등장, ...

print(val[0][0]) # 3
print(val[0][1]) # 10


# ==============================================
