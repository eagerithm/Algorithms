# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

# 입출력 예 설명

# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생

# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생

# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

# 나의 정답 : 장르별로 가장 많이 재생된 노래를 두 개씩 == 모든 장르에 대해 계산하라는 의미. 문제 똑바로 읽기.
def solution(genres, plays):
    info = {}
    genre_list = list(set(genres))

    for genre in genre_list:
        info[genre] = []
    
    for idx in range(len(genres)):
        info[genres[idx]].append((plays[idx], idx))
    
    sums = []
    for genre in genre_list:
        sums.append((sum(map(lambda x:x[0], info[genre])), genre))
    
    sums.sort(key = lambda x:x[0], reverse = True)
    
    answers = []
    for idx in range(len(genre_list)):
        genre = sums[idx][1]
        info[genre].sort(key=lambda x:(x[0], -x[1]), reverse=True)
        
        answers.append(info[genre][0][1])
        if len(info[genre]) > 1:
            answers.append(info[genre][1][1])
            
    return answers

# =================================================================
# 다른 사람의 풀이
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}

    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])

    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)

    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]

    return answer

# =================================================================
# 나의 오답 - 장르 내에서 가장 재생 횟수 높은 노래들이 서로 재생회수가 같은 경우, 같은 id 두개가 출력.
def solution(genres, plays):
    total_plays = {}
    each_plays = {}
    music_id = {}
    answer = []
    
    for i in range(len(genres)):
        if genres[i] not in total_plays.keys():
            total_plays[genres[i]] = 0 
            each_plays[genres[i]] = [] 

        total_plays[genres[i]] += plays[i]
        each_plays[genres[i]].append(plays[i])
        
        if (genres[i] + str(plays[i])) not in music_id.keys():            
            music_id[genres[i] + str(plays[i])] = i
    
    sorted_dict = sorted(total_plays.items(), key=lambda x: x[1], reverse = True)

    for (key, value) in sorted_dict:
        biggest_plays = sorted(each_plays[key], reverse = True)
        answer.append(music_id[key + str(biggest_plays[0])])           
        if len(biggest_plays) > 1:
            answer.append(music_id[key + str(biggest_plays[1])]) 
            
    return answer