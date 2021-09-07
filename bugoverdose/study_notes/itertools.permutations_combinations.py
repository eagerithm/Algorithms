# from itertools import permutations

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