# 도둑질
# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
# money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

# 입출력 예
# money	        return
# [1, 2, 3, 1]	4

# 나의 정답 - dp[k]과 k번째 집까지 들리면서 훔칠 수 있는 최대 금액
def solution(money):
    answer = 0   
    house_num = len(money) 
    
    # 0번째 집 훔치면서 시작
    stolen = [0] * (house_num-1) # 마지막 집은 대상에서 제외
    stolen[0] = money[0]
    stolen[1] = stolen[0] # 누적 금액이므로 1번째 집에서 동일 금액
    for i in range(2, house_num-1):
        stolen[i] = max(stolen[i-1], stolen[i-2] + money[i])
        # 이전 집 훔쳐서 못 훔치는 경우 vs 현재 들른 집 훔친 경우 중 최대 금액 선택
    answer = max(stolen)
    
    # 1번째 집 훔치면서 시작
    stolen = [0] * house_num
    stolen[1] = money[1] 
    stolen[2] = stolen[1]
    for i in range(3, house_num):
        stolen[i] = max(stolen[i-1], stolen[i-2] + money[i])
    answer = max(max(stolen), answer)    
    
    # start with idx = 2  - ex) [1 1 4 1 4] => 8이 최대?
    if house_num >= 5:
        stolen = [0] * house_num
        stolen[2] = money[2] 
        stolen[3] = stolen[2]
        for i in range(4, house_num):
            stolen[i] = max(stolen[i-1], stolen[i-2] + money[i])
    answer = max(max(stolen), answer)  
    
    return answer

# =================================================================
# stolen[i] = max(stolen[i-1], stolen[i-2] + money[i])의 원리 : 분기에 따른 선택지의 증가 + 이전 선택지들의 폐기

# [집] : 1 5 1 1  5  1  1  5
# 누적 : 0 5 5 6 10 10 11 15
# 선택     !   !              => 자연스럽게 폐기된 선택지
# 선택     !      !     !
# 선택     !      !        !  => 15

# =================================================================
# 다른 사람의 풀이
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)

# =================================================================