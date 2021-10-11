# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
# 다단계 칫솔 판매 (https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3)

def solution(enroll, referral, seller, amount):
    num = len(enroll)
    
    amount_sum = [0]*num
    
    sum_idx = {}    
    parent = {'center': 'center'}
    for idx in range(num):
        sum_idx[enroll[idx]] = idx       
        if referral[idx] == "-":
            parent[enroll[idx]] = 'center'
        else:
            parent[enroll[idx]] = referral[idx]
    
    sell_num = len(seller)
    for idx in range(sell_num):
        cur = seller[idx]
        cur_amount = amount[idx] * 100
        while parent[cur] != cur:
            pay_up = cur_amount//10
            amount_sum[sum_idx[cur]] += cur_amount - pay_up
            cur = parent[cur]
            cur_amount = pay_up
            if pay_up == 0: break # 시간초과 원인 제거
    
    return amount_sum

# =================================================================
def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    idx_list={}
    for idx,name in enumerate(enroll):
        idx_list[name]=idx
    for idx,name in enumerate(seller):
        price=100*amount[idx]
        answer[idx_list[name]]+=price
        while referral[idx_list[name]]!="-":
            answer[idx_list[name]]-=price//10
            name=referral[idx_list[name]]
            answer[idx_list[name]]+=price//10
            price=price//10
            if price==0:
                break
        answer[idx_list[name]]-=price//10
    return answer

# =================================================================