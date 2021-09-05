# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# 복수의 iterater들을 받아 같은 index의 데이터끼리 합친 tuple 생성.
# 최종 결과물의 데이터 수는 가장 크기가 작은 iterator의 크기와 동일.

# 참고. hash/02.py

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

# Output
{(2, 'two'), (3, 'three'), (1, 'one')}

# ================================================================
# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Output
[]

# ================================================================

numbersList = [1, 2, 3]
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

# Output
{(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}

# ================================================================

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

# Output
{(2, 'two', 'TWO'), (1, 'one', 'ONE')}

# ================================================================