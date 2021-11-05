# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.

# 입출력 예
# begin	target	words	                                    return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	        0

# 나의 정답2
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    possibles = list([begin]+words)
    length = len(possibles)
    word_len = len(begin)
    
    edges = {}
    for w in possibles:
        edges[w] = []
        
    for left in range(length):
        for right in range(left+1, length):
            mismatch = 0
            ok = True
            
            left_word = possibles[left]
            right_word = possibles[right]
            
            for idx in range(word_len):
                if left_word[idx] != right_word[idx]:
                    mismatch += 1
                if mismatch == 2: 
                    ok = False
                    break
            if ok:
                edges[left_word].append(right_word)
                edges[right_word].append(left_word)
    
    visited = {}
    for w in possibles:
        visited[w] = False
    
    queue = deque([(begin, 0)])
    counter = -1
    while queue:
        cur, counter = queue.popleft()
        visited[cur] = True
        if cur == target: break
        for next_word in edges[cur]:
            queue.append((next_word, counter+1))

    if visited[target]:
        return counter
    else:
        return 0

# =================================================================
# 나의 정답1
from collections import deque

def solution(begin, target, words):
    closest_distance = { begin: 0 }
    queue = deque([begin])
    
    while(queue):
        cur = queue.popleft()        
        for adjacent in get_adjacents(cur, words):
            if adjacent not in closest_distance: # 최초로 도달한 케이스만 기록. 최소 거리들만.
                closest_distance[adjacent] = closest_distance[cur] + 1
                queue.append(adjacent)
    
    return closest_distance.get(target, 0)

def get_adjacents(cur, words): 
    adjacents = []
    for word in words:
        if cur == words: 
            continue

        count = 0
        for i in range(len(word)):
            if cur[i] == word[i]:
                count += 1
                
        if count == len(word) - 1:
            adjacents.append(word)
    return adjacents

# =================================================================
# 다른 사람의 풀이 - BFS - 1-2-3과 1-3이 모두 존재하면 1-3만 고려.
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

# =================================================================
# 다른 사람의 풀이 
import heapq

def possible(A,B):
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    return count

def solution(begin, target, words):

    if not(target in words):
        return 0

    words.append(begin)

    network_dic = dict()

    for i in range(len(words)):
        network_dic[words[i]] = []
        for j in range(len(words)):
            if possible(words[i],words[j]) == len(begin) - 1:
                network_dic[words[i]].append(words[j])

    queue = [(0,begin)]

    while queue:

        length, node = heapq.heappop(queue)
        if node == target:
            return length
        if len(network_dic[node]) == 0:
            pass
        else :
            for i in network_dic[node]:
                if i != begin:
                    alt = length + 1
                    heapq.heappush(queue,(alt,i))

# =================================================================
