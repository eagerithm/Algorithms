# https://www.acmicpc.net/problem/11729
# 하노이 탑 이동 순서
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

# N개의 원판이 1번 장판에 주어졌을 때 3번 장판에 전부 옮기기
# A B : A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 의미

# 장판의 개수가 늘어나도 마지막 절차는 그대로 중복됨.

# 답 : C로 5개의 장판 옮겨서 쌓기 = B로 4개 옮기고, C로 5번째 장판 옮겨서 쌓기 
#    = C로 3개 옮기고, B로 4번째 옮겨서 쌓기 / C로 5번째 옮겨서 쌓기 ...
#    = B로 2개 옮기고, C로 3번째 옮겨서 쌓기 / B로 4번째 옮겨서 쌓기 / C로 5번째 장판 옮겨서 쌓기 ...
N = int(input())

# start에 꽂혀있는 num개의 원반을 by를 거쳐 end로 이동시킴
def moveHanoiTower(num, start, by, end, count, process):
        count += 1
        if num == 1: 
            process.append((start, end)) # // 원반의 수가 1개일 때는 그냥 옮기기
        else:
            # STEP 1 : 위의 작은 num-1개를 A에서 B로 이동
            count, process = moveHanoiTower(num-1, start, end, by, count, process) # 재귀 발생
            # STEP 2 : 가장 큰 1개를 최종목적지에 쌓기 : A에서 C로 이동
            process.append((start, end))
            # STEP 3 : 가장 큰 1개 위에 나머지 num-1개를 쌓기 : B에서 C로 이동
            count, process = moveHanoiTower(num-1, by, start, end, count, process)
        return (count, process)

count, process = moveHanoiTower(N, 1, 2, 3, 0, [])
print(count)
for p in process:
    print(p[0], p[1])

# =========================================