# 큐 2 (https://www.acmicpc.net/problem/18258)
# 파이썬의 리스트의 가장 앞 데이터를 쓰거나 지우면 리스트 내부의 전체 데이터를 다시 써주어야합니다. 가장 앞의 데이터를 지울 경우를 생각해보겠습니다. 해당 데이터를 지우고 전체 리스트의 데이터를 인덱스에 맞게 한칸씩 앞으로 당겨서 다시 써주어야합니다. 따라서 stacklist.pop(0)와 같이 가장 앞에 있는 리스트의 값을 pop시킬 경우, *_전체 리스트를 다시 써주어야하므로 시간 복잡도가 O(n)이 됩니다. *_그러므로 시간 초과로 문제를 해결할 수 없습니다.
# 따라서, 가장 앞을 가르키는 인덱스 값을 가지고 있는 것입니다. 위의 소스코드의 cnt가 해당 역할을 합니다. pop기능을 수행하면 가장 앞 인덱스 cnt에 해당되는 부분을 출력하고 cnt에 1을 더해서 가장 앞쪽을 가르키는 인덱스를 그 다음 칸을 가르키도록 합니다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.

# 나의 정답 - 큐의 출구를 가르키는 index를 만들기
import sys

input = sys.stdin.readline

queue = [0]*2000000
front_idx = 0
back_idx = 0
empty = 1 # 비어있으면 1, 아니면 0을 출력

for _ in range(int(input())):
    command = input().rstrip()

    if command[0:3] == "pop":
        if empty == 1:
            print(-1)
        else:
            print(queue[front_idx])
            if front_idx == back_idx:
                empty = 1
            else:
                front_idx += 1 
    elif command[0:4] == "push":
        if empty == 1:
            empty = 0
            queue[back_idx] = int(command.split()[1])
        else:
            back_idx += 1
            queue[back_idx] = int(command.split()[1])
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
# 시간초과
import sys

input = sys.stdin.readline
print = sys.stdout.write

queue = []
length = 0

for _ in range(int(input())):
    command = input().rstrip()

    if command[0:3] == "pop":
        if queue:
            print(queue[0])
            length -= 1
            queue = queue[1:]
        else:
            print('-1')                
    elif command[0:4] == "size":
        print(str(length))
    elif command[0:4] == "back":
        print(queue[-1] if queue else '-1')
    elif command[0:5] == "empty":
        print('0' if queue else '1')
    elif command[0:5] == "front":
        print(queue[0] if queue else '-1')    
    

    if command[0:4] == "push":
        length += 1
        queue.append(command[5:])
    else:
        print('\n')

# ==========================================================