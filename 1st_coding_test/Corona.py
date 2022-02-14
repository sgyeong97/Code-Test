#8번 문제
def solution(history, infected):
    building = []
    result = []
    start = False
    for x in history:
        if x == infected:
            start = True
            continue
        elif x == (-infected):
            result += set(building)
            return sorted(result)
        else:
            if x > 0:
                building.append(x)
            else:
                index = building.index(-x)
                temp = building.pop(index)
                if start:
                    result.append(temp)

# test_case = [[3,2,-3,1,-1,-2,4,-4,1,-1], 2]
# test_case = [[1,3,2,-1,-2,-3,4,-4], 2]
test_case = [[2,3,4,-2,-3,-4,1,-1], 2]
# print(solution[test_case[0], test_case[1]])
result = solution(test_case[0], test_case[1])
print(result)