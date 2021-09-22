# map + sum 조합으로 각 요소에 대해 lambda 적용한 결과 반환받고 합치기

# Count even numbers in the list
listOfElems = [11, 22, 33, 45, 66, 77, 88, 99, 101]

count = sum(map(lambda x:x%2==0, listOfElems))

print('Count of even numbers in a list : ', count)
# Count of even numbers in a list :  3

# ====================================================
# sum은 True를 1로 간주하여 합산하게 됨

print(list(map(lambda x : x%2 == 0, listOfElems)))
# [False, True, False, False, True, False, True, False, False]
 
print(sum([True, False, True])) # 2

# ====================================================
bigger_count = []

nums = list(map(int, input().split())) # 2 4 -10 4 -9

for num in nums:
    bigger_count.append(sum(map(lambda x:num>x, nums)))

print(' '.join(map(str, bigger_count))) # 2 3 0 3 1

# ====================================================