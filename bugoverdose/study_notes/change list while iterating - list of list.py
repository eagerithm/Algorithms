# list(list(~)) : 변하지 않는 복제 리스트를 순회하며, 원본을 제거
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
for elem in list(list_of_num):
    if elem == 54 or elem == 55:
        list_of_num.remove(elem)

print(list_of_num)
# [51, 52, 53, 56, 57, 58, 59]

# ==============================================
# 문제 : 순회 과정에서 index=3 실행 후 index=4 실행시, 54 => 56으로 건너뛰게 됨.
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
for elem in list_of_num:
    if elem == 54 or elem == 55:
        list_of_num.remove(elem)

print(list_of_num)
# [51, 52, 53, 55, 56, 57, 58, 59]

# ==============================================
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove all occurrences of 54 & 55 from list
list_of_num = list(filter(lambda num: num != 54 and num !=55,
                          list_of_num)
                   )
print(list_of_num)
# [51, 52, 53, 56, 57, 58, 59]

# ==============================================