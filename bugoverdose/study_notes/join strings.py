# The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with space : 각 문자열 요소 사이에 공백 한칸씩(' ') 존재하는 형식으로 합치기
print(' '.join(text))
# Python is a fun programming language

# for문으로 하나씩 조회하고 +=로 합치는 것과 결과는 동일
<<<<<<< HEAD
=======

# ===================================================================
numbers = "10548123"

biggest_num = int(''.join(sorted(map(str, list(numbers)), reverse = True))) # 무의미한 str(number). 문자열 => 문자열
# 85432110
biggest_num = int(''.join(sorted(list(numbers), reverse = True)))
# 85432110

# ===================================================================
>>>>>>> bugoverdose/210906
