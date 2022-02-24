#No.5
def solution(distance, time):
    enemy = []
    defance = 0
    attack = 0
    for x in range(len(distance)):
        empty = distance[x]/time[x]
        enemy.append(int(empty))

    for round in range(1, max(enemy)+1):
        defance += 1
        attack += enemy.count(round)
        if defance < attack:
            return -1
    return defance-attack

if __name__ == '__main__':
    # test_case = [[1,2,8],[1,1,2],1]
    test_case = [[2,2,3,6],[1,1,1,2],-1]
    # test_case = [[1,1],[1,1],-1]
    # test_case = [[3,3],[1,1],1]
    # test_case = [[1,5,7],[1,2,3],-1]
    # test_case = [[3,3,3],[1,1,1],0]
    result = solution(test_case[0], test_case[1])
    if result == test_case[2]:
        print(f"Success [{result}]")
    else:
        print(f"Fail [{result}]")