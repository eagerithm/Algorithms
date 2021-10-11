# Summer/Winter Coding(2019)
# 멀쩡한 사각형 (https://programmers.co.kr/learn/courses/30/lessons/62048)

import math

def solution(w,h):
    answer = w*h
    times = math.gcd(w,h) # 최대공약수 - 시간초과 예방
    w //= times
    h //= times
    
    sub = 0
    if w < h: # 시간초과 예방
        for idx in range(w):
            top = h*w - h*idx
            cur_h = top//w if top%w == 0 else (top//w)+1
            next_h = (top-h)//w
            sub += (cur_h - next_h)
    else:
        for idx in range(h):
            top = h*w - w*idx
            cur_w = top//h if top%h == 0 else (top//h)+1
            next_w = (top-w)//h
            sub += (cur_w - next_w)
            
    return answer - sub*times

# =================================================================