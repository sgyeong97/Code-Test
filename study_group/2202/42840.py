def solution(answers):
    answer = []
    score = [0,0,0]
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    index = 0
    max = 0
    for a in answers:
        if a == stu1[index%len(stu1)]:
            score[0] += 1
        if a == stu2[index%len(stu2)]:
            score[1] += 1
        if a == stu3[index%len(stu3)]:
            score[2] += 1
        index += 1
    max = sorted(score)[-1]
    for x in range(3):
        if max == score[x]:
            answer.append(x+1)
    return answer

test_case = [1,2,3,4,5]
# test_case = [1,3,2,4,2]
print(solution(test_case))