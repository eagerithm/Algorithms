# input() : 입력값 한 줄 받기 # 입력값이 여러줄인 경우 각 줄에 대해 일일이 실행하여 받을 수도 있음

score = int(input()) # ex) 90

grade = 'F'
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
    
print(grade)

# ==============================================
# input().split() : 입력값 한 줄을 문자열로 받고, 공백을 기준으로 나누기(양끝 공백은 자동 trim)
# .split(", ") : ', '를 기준으로 나눠서 받기. 문자열 사이의 쉼표와 공백은 제거

# ex) 95 5 
A, B = map(int, input().split())  # 몇개의 요소인지 사전에 알 수 있으면 각 변수에 담을 수 있음.
# list = list(map(int, input().split())) # set(), list() 등으로 다시 감싸서 사용
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# ==============================================
# open(0) : 입력되는 파일의 각 줄을 개별적으로 받기
# ex) 951 
#     123
 
A, B = map(int, open(0)) 
i = 0
sum = 0
for num in list(str(B))[::-1]:
    cur = A * int(num)
    print(cur)
    sum += cur * (10 ** i)
    i += 1
print(sum)

# ==============================================
# cf) bad example : input은 한줄만 입력받고, 다음줄로 커서 이동 
data = input().split('\n')
print(data)

# stdin 
# 5
# 1 1
# 2 3

# stdout 
# ['5']

# ==============================================
# 한줄씩 입력받을 때 성능개선 : input 대신 sys.stdin.readline을 사용
# 마찬가지로 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 `문자열을 저장`하고 싶을 경우 .rstrip()을 추가로 해주는 것이 좋다.

# rstrip을 하라는 건 `문자열` 자체를 변수에 저장하고 싶을 때 얘기지, 
# 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다. 
# 즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다. 
# 참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

# sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
import sys
a = sys.stdin.readline().rstrip()
# stdin  : 3
# stdout : 3\n   => 문자열 그대로 사용하고 싶은 경우 개행문자까지 포함됨 
# .rstrip()로 제거안하면 매 입력값마다 \n 적용됨. print 사용시 \n 두번 적용됨

# ==============================================
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    
    if A == 0 and B == 0: 
        break
    print(A+B)   

# ==============================================
import sys

for line in sys.stdin:
    stack = []
    is_vps = True
    string = line.rstrip() # 문자열 끝의 \n 제거
    print(list(string))

# ==============================================