import sys

def solution(city):
    city_index = []
    bus_station = []
    for x in range(len(city)):
        temp = []
        for y in range(len(city[x])): 
                temp.append([x,y])
                if city[x][y] == 0:
                    bus_station.append([x,y])
        city_index.append(temp)

    for x in range(len(city_index)):
        count = 0
        for city_x, city_y in city_index[x]:
            min = sys.maxsize
            for bus_x, bus_y in bus_station:
                distance = abs(city_x - bus_x) + abs(city_y - bus_y)
                if min > distance:
                    min = distance
            city_index[x][count] = min
            count += 1
    return city_index

city = [[1,0,1,1],[1,1,1,1],[1,1,0,1],[1,1,1,1]]
result = solution(city)
print(result)