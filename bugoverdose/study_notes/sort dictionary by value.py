# sorted(dictionary.items(), key=lambda x: x[1])

def solution(genres, plays):
    total_plays = {}
    each_plays = {}
    
    for i in range(len(genres)):
        if genres[i] not in total_plays.keys():
            total_plays[genres[i]] = 0 
            each_plays[genres[i]] = [] 

        total_plays[genres[i]] += plays[i]
        each_plays[genres[i]].append(plays[i])
        
    # total_plays dictionary의 item들(key-value쌍들)에 대해 value 값을 기준으로 DESC 정렬
    sorted_dict = sorted(total_plays.items(), key=lambda x: x[1], reverse = True)

    # sorted(list, reverse = True) : 리스트의 각 요소를 DESC 정렬
    for (key, value) in sorted_dict:
        biggest_plays = sorted(each_plays[key], reverse = True)