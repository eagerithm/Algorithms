# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name	      return
# "JEROEN"	  56
# "JAN"	      23
# "ZZAAAZZ"   8

# 나의 정답2
def solution(name):
    name = list(name)
    length = len(name)
    result = ["A"]*length
    
    abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dic_abc = {}
    for i in range(26):
        dic_abc[abc[i]] = min(i, 26-i)
    
    count = 0
    idx = 0
    
    while True:
        if result[idx] != name[idx]:
            count += dic_abc[name[idx]]
            result[idx] = name[idx]

        if result == name: break
        
        next_idx = -1
        for i in range(1, length):
            next_idx = (idx+i)%length
            if result[next_idx] != name[next_idx]:
                idx = next_idx
                count += i
                break
                
            next_idx = (idx-i+length)%length
            if result[next_idx] != name[next_idx]:
                idx = next_idx
                count += i
                break 
    
    return count

# =================================================================
# 나의 정답1
def solution(name):
    answer = 0
    d = {}
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    for i in range(len(alphabets)):
        d[alphabets[i]] = min(i, 26 - i) 
    
    # 각 인덱스에 도달했을 때 수행되어야 하는 작업량 지정 => 해당 인덱스 도달 여부까지 함께 체크
    target_per_index = [0] * len(name) 
    
    for i in range(len(name)):
        target_per_index[i] = d[name[i]]

    cur_index = 0
        
    while True:
        answer += target_per_index[cur_index]
        target_per_index[cur_index] = 0
        
        if sum(target_per_index) == 0:
            break
            
        left = 1
        right = 1

        while target_per_index[cur_index - left] == 0:
            left += 1
        while target_per_index[cur_index + right] == 0:
            right += 1

        answer += min(left, right)

        if (left < right):
            cur_index -= left
        else:
            cur_index += right

    return answer

# =================================================================
# 다른 사람의 풀이 
def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]

    answer = 0
    where = 0

    while True:
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer

# =================================================================
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = {}

for i in range(len(alpha)): # 가장 세련된 방법
    d[alpha[i]] = min(i, 26-i)  

# =================================================================
def alphabet_to_num(char): 
    num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)] 
    return num_char[ord(char) - ord('A')] 
# num_char = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ord('A') == 65 # returns an integer representing the Unicode character.

# =================================================================
# 틀린 풀이 - 10/11 : "ZZAAAZZ" => 8처럼 왔던 곳을 되돌아가는게 이득인 경우 간과
def solution(name):
    answers = []
    
    abc_no_a = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_front = "ABCDEFGHIJKLMN"
    abc_back = "OPQRSTUVWXYZA"
    abc_dic = {}
    
    for i in range(len(abc_front)):
        cur = abc_front[i]
        abc_dic[cur] = i
    
    for i in range(len(abc_back)):
        cur = abc_back[len(abc_back) - i - 1]
        abc_dic[cur] = i
    
    answer = calculate(name, list(name), abc_dic, abc_no_a)
    answers.append(answer)
    
    answer = calculate(name, [name[0]] + list(name)[::-1][:-1], abc_dic, abc_no_a)
    answers.append(answer)
    
    return min(answers)

def calculate(name, target_list, abc_dic, abc_no_a):
    answer = len(name) - 1
    while target_list:
        if any(item in target_list for item in list(abc_no_a)):
            target = target_list.pop(0)
            answer += abc_dic[target]
        else:
            answer -= len(target_list)
            break
    return answer

# =================================================================