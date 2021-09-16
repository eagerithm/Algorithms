# 단속카메라
# 고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# 차량의 대수는 1대 이상 10,000대 이하입니다.
# routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
# 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

# 입출력 예
# routes	                                return
# [[-20,15], [-14,-5], [-18,-13], [-5,-3]]	2

# 나의 정답
def solution(routes):    
    routes.sort(key = lambda x:(x[0],x[1]))
    left = routes[0][0]
    right = routes[0][1]
    answer = 1
    
    if len(routes) == 1:
        return answer
    
    for route in routes[1:]:
        cur_l, cur_r = route
        
        if right < cur_l:
            left = cur_l
            right = cur_r
            answer += 1
            continue
            
        if cur_r < right: 
            right = cur_r
        
        if cur_l < right:
            left = cur_l
            
    return answer

# =================================================================
# 다른 사람의 풀이
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
    
# =================================================================