#4¹ø ¹®Á¦
def solution(n):
    max = 1
    if n < 2:
        return max
    for x in range(n):
        empty = x*x*x
        if empty > n:
            return max
        elif max < empty:
            max = empty