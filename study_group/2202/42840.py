def solution(answers):
    answer = []
    score = []
    max = 0
    stu = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for x in range(3):
        score.append(get_score(answers, stu[x], 0))        
        if max < score[x]:
            max = score[x]
    for x in range(3):
        if max == score[x]:
            answer.append(x+1)
    return sorted(answer)

def get_score(answers, stu, index):
    if len(answers) <= index:
        return 0
    if answers[index] == stu[index%len(stu)]:
        return 1 + get_score(answers, stu, index+1)
    else:
        return 0 + get_score(answers, stu, index+1)

test_case = [1,2,3,4,5]
# test_case = [1,3,2,4,2]
print(solution(test_case))