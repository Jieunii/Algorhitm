def solution(genres, plays):
    answer = []
    album = {}
    total = {}
    for i in range(len(genres)):
        if genres[i] not in album.keys():
            album[genres[i]] = [(plays[i], i)]
            total[genres[i]] = plays[i]
        else:
            album[genres[i]].append((plays[i], i))
            total[genres[i]] += plays[i]
    total = sorted(total.items(), key=(lambda x:x[1]), reverse=True)
    
    for genre in total:
        play_list = album[genre[0]]
        # 첫번째 원소로 내림차순 정렬하고 첫번째 원소가 같은 경우 두번째 원소로 오름차순
        play_list = sorted(play_list, key=lambda x:(-x[0], x[1])) 
        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])
    
    return answer