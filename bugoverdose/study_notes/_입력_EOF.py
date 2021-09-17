# https://www.acmicpc.net/board/view/28332

# 더 이상 입력값이 없을 때 input 등으로 읽으려고 하면 에러 발생
# 입력값의 줄 개수 판단할 수 없으면 try-except문 사용

while True:
    try :
        line = input()
        # ...
    except EOFError:
        break

# ==============================================
# 입력되는 모든 줄에 대해 동일 작업 수행하는 경우. 입력값이 많은 경우.
import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    print(A+B)

print('자동으로 맨 마지막 입력 받고 탈출')

# ==============================================
import sys

while True:
    input_ = sys.stdin.readline()
    if input_ == '':
        break
    print(type(input_))
    sys.stdout.write(input_)

# ==============================================
