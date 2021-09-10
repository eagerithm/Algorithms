# sort와 sorted 모두 각 요소에 대해 key를 실행한 결과들을 기준으로 리스트 요소들 정렬 가능. 
str_list = ['좋은하루','good_morning','굿모닝','niceday']

print(sorted(str_list, key=len))  # 함수
# ['굿모닝', '좋은하루', 'niceday', 'good_morning']

print(sorted(str_list, key=lambda x : x[1]))  # 람다
# ['niceday', 'good_morning', '굿모닝', '좋은하루']

# ==============================================================
# .sort(key = ~~) 방식으로 원본 수정도 가능
num_list = [15, 22, 8, 79, 10]
num_list.sort()
print(num_list) # [8, 10, 15, 22, 79]

tuple_list = [('좋은하루', 0),
              ('niceday', 1), 
              ('좋은하루', 5), 
              ('good_morning', 3), 
              ('niceday',5)]

# 복수의 정렬 기준이 순차적으로 모두 적용되도록 key 값으로 tuple 반환하도록 지정 가능
tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
print(tuple_list)
# [('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]

# ==============================================================
# 복수의 정렬 기준은 () 내부에 나열
jobs = [[0, 3], [1, 9], [2, 6]] 
todos = sorted(jobs, key = lambda x:(x[0], x[1])) 
# index=0 기준 정렬 후, index=1 기준 정렬

# ==============================================================