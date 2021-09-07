enumerate(iterable, start=0)
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0

# (index, 원본값)들로 구성된 enumerate (일종의 리스트)로 변형

# =========================================================
score = [0, 5, 5]
result = []

for idx, s in enumerate(score): # [0, 5, 5] => [(0,0), (1,5), (2,5)]
    if s == max(score):
        result.append(idx+1)


for idx, s in enumerate(score, 1): # [0, 5, 5] => [(1,0), (2,5), (3,5)]
    if s == max(score):
        result.append(idx)

# =========================================================
l1 = ["eat","sleep","repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
# Return type: < type 'enumerate' >

print (list(enumerate(l1)))
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
 
# start index = 2
print (list(enumerate(s1, 2)))
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

# =========================================================