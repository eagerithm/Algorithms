from math import pi

R = int(input()) # 2

print(pi * (R ** 2)) # 3.141593   # 유클리드 기하학에서 원의 정의
print(2 * (R ** 2)/1) # 2.0       # 비유클리드 기하학 중 택시 기하학

# ==============================================
import math

string = input() # OneTwoThreeFourFiveSixSevenEightNineTen

N = math.ceil(len(string)/10) # len(string) = 39 # N = 4

for idx in range(N):
    print(string[idx*10:(idx+1)*10])
    # OneTwoThre
    # eFourFiveS
    # ixSevenEig
    # htNineTen
