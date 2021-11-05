# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 입출력 예제
# phone_book                         return
# ["119", "97674223", "1195524421"]  false
# ["123","456","789"]                true
# ["12","123","1235","567","88"]     false

# cf) 리스트 내림차 정렬 : phone_book.sort(reverse = True)

# 나의 정답2
def solution(phone_book):
    phone_book.sort()
    for idx in range(1, len(phone_book)):
        pre = phone_book[idx-1]
        if pre == phone_book[idx][:len(pre)]:
            return False
    return True

# =================================================================
# 나의 정답1
def solution(phone_book):
    answer = True
    sorted_list = sorted(phone_book)
    prev = sorted_list[0]

    for i in range(1, len(sorted_list)):
        cur = sorted_list[i]
        if(cur.startswith(prev)):
            answer = False
            break
        prev = cur

    return answer

# =================================================================
# 다른 사람의 풀이 : zip function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# =================================================================
