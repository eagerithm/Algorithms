# 회의실 배정 (https://www.acmicpc.net/problem/1931)
# 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
# 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

# 나의 정답
import sys

input = sys.stdin.readline

meetings = []
N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x:(x[0], x[1]))

count = 0
prev_end = -1
cur_end = -1

for idx in range(N):
    start, end = meetings[idx]
    if start < prev_end: continue

    if cur_end <= start:
        prev_end = cur_end
        cur_end = end
        count += 1 # 결과적으로 다른 구간의 회의를 사용하더라도 일단 영역 기준 추가
    elif end < cur_end: # and start < cur_end
        cur_end = end

print(count)

# =================================================================
# -1 -1
# -1 6  (0, 6) # cur_end < start일 때 cur_end 대체
# -1 4  (1, 4) # end < cur_end일 때 cur_end 대체
# -1 4  (2, 13)
# -1 4  (3, 5)
# -1 4  (3, 8)
#  4 7 (5, 7) # cur_end < start일 때 cur_end 대체 + prev_end로 변경
#  4 7 (5, 9)
#  4 7 (6, 10)
#  7 11 (8, 11) 
#  7 11 (8, 12) 
#  11 14 (12, 14)

# =================================================================
# 다른 사람의 풀이
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    dic = {}
    for _ in range(N):
        start, end = map(int, input().split())
        if dic.get(start):
            dic[start].append(end)  # min(dic.get(start, float('inf')), end)
        else:
            dic[start] = [end]
    
    for k in dic.keys():
        dic[k].sort()
        
    keys = sorted(dic.keys())
    end = 0
    count = 0
    for key in keys:
        for e in dic[key]:
            if e < end:
                end = e
            elif key >= end:
                count += 1
                end = e
    print(count)

solve()

# =================================================================