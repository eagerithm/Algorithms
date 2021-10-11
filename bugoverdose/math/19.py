# 찾아라 프로그래밍 마에스터
# 폰켓몬 (https://programmers.co.kr/learn/courses/30/lessons/1845)

def solution(nums):
    answer = 0
    nums.sort()
    prev = -1
    for num in nums:
        if num != prev:
            answer += 1
            prev = num
        if answer == len(nums)//2: break
    
    return answer

# =================================================================