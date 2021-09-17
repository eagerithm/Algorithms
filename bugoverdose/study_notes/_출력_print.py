# 복수의 인자를 받으면 공백으로 나눔 
print("A", "B", 12)
# A B 12
# ==============================================
animals = 'eels'

print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.

print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.
# ==============================================
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i+1}: {A+B}')
# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7
# ==============================================
# 문자열.format()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

# ==============================================
# 소수점은 f'~{number:.2f}' 형식으로 2번째 소수점까지 표시(3번째에서 반올림)

import sys

for line in sys.stdin:
    scores = list(map(int, line.split()))
    scores.pop(0)
    scores.sort(reverse = True)
    average = sum(scores)/len(scores)
    above_average = 0
    for score in scores:
        if score > average:
            above_average += 1
        else:
            break
            
    above_average_ratio = above_average/len(scores)*100
    print(f'{above_average_ratio:.3f}%')

# ==============================================