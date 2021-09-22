
from itertools import permutations
 
# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

for i in list(perm):
    print (i)
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)

# =====================================
# combinations vs permutations

from itertools import combinations
a = [1,2,3]
combi = combinations(a,2)
print(list(combi)) # [(1,2),(1,3),(2,3)]

from itertools import permutations
a = [1,2,3]
permute = permutations(a,2)
print(list(permute)) # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# =====================================
from itertools import product
a = [1,2,3]
b = [4,5,6]

prod1 = product(a,a,b) # itertools.product(*iterables) # 모든 리스트들과 각각 조합
print(list(prod1))
# [(1, 1, 4), (1, 1, 5), (1, 1, 6), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (2, 1, 4), (2, 1, 5), (2, 1, 6), (2, 2, 4), (2, 2, 5), (2, 2, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (3, 1, 4), (3, 1, 5), (3, 1, 6), (3, 2, 4), (3, 2, 5), (3, 2, 6), (3, 3, 4), (3, 3, 5), (3, 3, 6)]

prod2 = product(a,repeat = 2) # product(*iterables, repeat=M) 자기 자신들과 M번 조합
print(list(prod2)) 
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# =====================================