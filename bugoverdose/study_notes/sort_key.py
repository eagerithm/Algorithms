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
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
import sys

input = sys.stdin.readline

members = []

for i in range(int(input())):
    x, y = input().split()
    members.append([i, int(x), y])

for i in sorted(members, key=lambda x:(x[1],x[0])):
    print(i[1], i[2])
    
# 3            (input)
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

# 20 Sunyoung  (output)
# 21 Junkyu
# 21 Dohyun
# ==============================================================