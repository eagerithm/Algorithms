ord("c") # "c"의 ascii 코드 반환

c = 'p'

print("The ASCII value of '" + c + "' is", ord(c))
# The ASCII value of 'p' is 112

# ==============================================
chr(65)           # 'A' # ascii 코드에 대응되는 문자값 반환
chr(120)          # 'x'
chr(ord('S') + 1) # 'T'

# ==============================================
# ==============================================
targets = list("baekjoon")
first_appearance = [-1] * 26

for idx in range(len(targets)):
    abc_idx = ord(targets[idx]) - 97 # ord('a') # 97
    
    if first_appearance[abc_idx] == -1:
        first_appearance[abc_idx] = idx

print(" ".join(list(map(str, first_appearance))))
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# ==============================================
dic = {}

for letter in list(input()):
    ascii = ord(letter)
    if ascii >= 97:
        ascii -= 32
    letter = chr(ascii)
    
    if letter not in dic.keys():
        dic[letter] = 1
    else:
        dic[letter] += 1
        
occured = list(dic.keys())
occurrences = list(dic.values())
max_occurrence = max(occurrences)

if occurrences.count(max_occurrence) >= 2:
    print("?")
else:
    max_idx = occurrences.index(max_occurrence)
    print(occured[max_idx])

# Mississipi # ?
# zZa        # Z
# z          # Z

# ==============================================