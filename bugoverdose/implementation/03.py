# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
# 로또의 최고 순위와 최저 순위 (https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3)
# 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 
# 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
# 알아볼 수 없는 번호를 0으로 표기

def solution(lottos, win_nums):
    max_count = 0
    min_count = 0
    answer = []
    
    for l in lottos:
        if l == 0 :
            max_count += 1
            continue        
        if l in win_nums:
            max_count += 1
            min_count += 1
            continue

    if max_count > 1:
        answer.append(7-max_count)
    else:
        answer.append(6)
        
    if min_count > 1:
        answer.append(7-min_count)
    else:
        answer.append(6)

    return answer

# =================================================================
# 입력: [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]	
# 출력: [3, 5]
# =================================================================
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# =================================================================