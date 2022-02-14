#9번 문제

def solution(lineUp, level):
    distance = -1
    for x in lineUp:
        if (distance == -1):
            if x:
                distance = 0
        else:
            if not(x):
                distance += 1
            else:
                if distance < level:
                    return False
                else:
                    distance = 0
    return True

# test_case = [[1,0,0,0,1,0,0,1], 2]
test_case = [[1,0,0,1,0,1,0,0,0,1], 2]
print(solution(test_case[0], test_case[1]))