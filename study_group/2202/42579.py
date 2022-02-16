def solution(genres, plays):
    answer = []
    sort_list = []
    count_list = []
    start_list = []
    #장르 중복 제거, 이름 리스트 생성
    genres_names = list(set(genres))
    #장르별 정렬 리스트, play 횟수 체크 리스트 생성
    for x in range(len(genres_names)):
        sort_list.append([x])
        count_list.append(0)
    # 장르별 이름 리스트 인덱스 수에 맞게 정렬리스트에 정리 및 play횟수 total 수집
    for count in range(len(plays)):
        index = genres_names.index(genres[count])
        sort_list[index].append([count, plays[count]])
        count_list[index] += plays[count]
    max = sorted(count_list, reverse=True)
    #count 횟수를 기반으로 장르별 순서를 기반으로한 start_list 생성
    while(1):
        if max == []: break
        else:
            index = count_list.index(max[0])
            max.pop(0)
            start_list.append(index)
    #start리스트를 기반으로 answer에 넣을 곡 index 선별
    for index in range(len(start_list)):
        # [노래카테고리, [index, plays], [index, plays]] 형식의 sorted에서 [index,plays]들만 리스트화
        temp = sorted(sort_list[start_list[index]][1:])
        # lambda를 이용한 2차원 배열 2번째 요소 기준 정렬 (2번째요소->1번째요소 순으로 정렬)
        temp.sort(key=lambda x:-x[1])
        # 2곡 이상이 있는 곡들 선별
        if(len(temp)>1):
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            #한곡밖에 없을 경우 선별
            answer.append(temp[0][0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))