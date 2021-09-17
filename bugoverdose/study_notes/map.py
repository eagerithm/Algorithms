# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 해당 람다식을 commands 리스트의 각 요소에 대해 적용한 결과 반환
# 중요 : list(), set() 등으로 감싸줘야 함!!!
mapped_result = list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(mapped_result) # [5, 6, 3]
