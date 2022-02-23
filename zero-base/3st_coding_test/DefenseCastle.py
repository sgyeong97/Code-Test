#5¹ø ¹®Á¦
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