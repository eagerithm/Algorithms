# 덱 (https://www.acmicpc.net/problem/10866)

# 나의 정답
import sys

input = sys.stdin.readline

queue = [0]*30000
front_idx = 10000
back_idx = 10000
empty = 1 # 비어있으면 1, 아니면 0을 출력

for _ in range(int(input())):
    command = input()

    if command[0:3] == "pop":
        if empty == 1:
            print(-1)
        else:
            if command[0:9] == "pop_front":
                print(queue[front_idx])
                if front_idx == back_idx:
                    empty = 1
                else:
                    front_idx += 1 
            else:
                print(queue[back_idx])
                if front_idx == back_idx:
                    empty = 1
                else:
                    back_idx -= 1

    elif command[0:4] == "push":
        is_front = command[0:10] == "push_front"

        if empty == 1:
            empty = 0
        else:
            if is_front:
                front_idx -= 1
            else:
                back_idx += 1
        queue[front_idx if is_front else back_idx] = int(command.split()[1])

    elif command[0:4] == "size":
        if empty == 1:
            print(0)
        else:
            print(back_idx - front_idx + 1)
    elif command[0:4] == "back":
        if empty == 1:
            print(-1)
        else:
            print(queue[back_idx])
    elif command[0:5] == "empty":
        print(empty)
    else:
        if empty == 1:
            print(-1)
        else:
            print(queue[front_idx]) 
    
# ==========================================================