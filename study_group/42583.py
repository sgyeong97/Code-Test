def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    pass_truck = []
    total_truck = len(truck_weights)
    while(1):
        #트럭이 다리를 모두 건넌 경우
        if (len(pass_truck) == total_truck):
            return answer
        #트럭이 다리를 다 못 건너간 경우
        else:
            #bridge 스택이 bridge_length 이상일 경우
            if (len(bridge) >= bridge_length):
                #트럭이 지나간 경우 pass_truck에 지나간 트럭 추가
                if(bridge[0] != 0):
                    pass_truck.append(bridge[0])
                #지나간 트럭 또는 못 지나가서 비어있도 stack에 추가되어서 추가된 값 제거
                bridge.pop(0)
            #기다리고 있는 트럭이 있는 경우
            if truck_weights:
                #일단 기다리고 있는 트럭이 다리위로 올라갔을때를 가정
                bridge.append(truck_weights.pop(0))
                #트럭이 올라갔을 때 무게가 초과했을 경우
                if(sum(bridge) > weight):
                    #트럭을 다시 대기열 앞 순위로 지정
                    truck_weights.insert(0, bridge.pop())
                    #트럭이 못 올라감을 0으로 표현
                    bridge.append(0)
            #기다리고 있는 트럭이 없지만 앞에 지나가고 있는 트럭이 있을 경우 현재 새로 올라간 트럭이 없음을 0으로 명시
            else:
                bridge.append(0)
        answer += 1