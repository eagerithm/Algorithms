# 문제 설명
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

# 예를들어
# 0ms 시점에 3ms가 소요되는 A작업 요청
# 1ms 시점에 9ms가 소요되는 B작업 요청
# 2ms 시점에 6ms가 소요되는 C작업 요청

# 한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.

# A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
# B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
# C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)

# 이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

# 하지만 A → C → B 순서대로 처리하면
# A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
# C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
# B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
# 이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

# 제한 사항
# jobs의 길이는 1 이상 500 이하입니다.
# jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
# 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
# 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

# 입출력 예
# jobs	                    return
# [[0, 3], [1, 9], [2, 6]]	9
# 입출력 예 설명
# 0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
# 1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
# 2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.

# 나의 정답 
import heapq # from heapq import heappush, heappop
def solution(jobs):
    answer = 0
    heap = []
    todos = sorted(jobs, key = lambda x:(x[0], x[1])) # index=0 기준 정렬 후, index=1 기준 정렬
    time_passed = 0
    
    while(todos or heap): # 둘 중 하나라도 비어있지 않다면 계속 진행
        while(todos and todos[0][0] <= time_passed): # 현 시점에서 실행가능해진 작업들 전부 heap에 추가
            start, duration = todos.pop(0)
            heapq.heappush(heap, [duration, start])
        
        if(len(heap) == 0): # 힙이 비어있다면 들어있던 작업들이 막 끝난 시점
            start, duration = todos.pop(0)
            heapq.heappush(heap, [duration, start])
            time_passed = start # (1) 다음 작업 시작 가능 시점으로 이동

        # 힙에 있는 작업 하나를 꺼내어 끝까지 처리
        duration, start = heapq.heappop(heap)
        time_passed += duration # (1) 처리 종료 시점으로 이동 # (1)들 대체 가능: time_passed = max(time_passed + duration, start + duration) 
        answer += time_passed - start
        
    return int(answer / len(jobs))

# ======================================================
# 다른 사람의 풀이
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    
    current_time = 0
    total_response_time = 0
    
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
            
    return total_response_time // len(jobs)

# ======================================================