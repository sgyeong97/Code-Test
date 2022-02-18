def solution(lottos, win_nums):
    answer = []
    grade = [6,5,4,3,2,1]
    joker = lottos.count(0)
    count = 0
    for x in win_nums:
        if x in lottos:
            count += 1
    top = count+joker
    low = count
    if top == 0 and low == 0:
        answer = [6,6]
    elif low == 0 :
        answer = [grade.index(top)+1, 6]
    else:
        answer = [grade.index(top)+1, grade.index(low)+1]
    return answer