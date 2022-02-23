import sys

def solution(area):
    result = []
    min = sys.maxsize
    for w in range(1, area+1):
        if not(area % w):
            h = int(area/w)
            if (h >= w):
                if min > abs(h-w):
                    result = [w, h]
    return result

# area = 4
# area = 100
# area = 51312
area = 87465
print(solution(area))