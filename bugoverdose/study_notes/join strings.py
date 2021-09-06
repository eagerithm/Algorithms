# The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with space : 각 문자열 요소 사이에 공백 한칸씩(' ') 존재하는 형식으로 합치기
print(' '.join(text))
# Python is a fun programming language

# for문으로 하나씩 조회하고 +=로 합치는 것과 결과는 동일
