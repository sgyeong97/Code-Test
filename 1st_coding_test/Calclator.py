def solution(s):
    result = 0
    temp = ''
    sign = ''

    for x in s:
        if x == '-' or x == '+':
            if not(temp):
                sign = x
                continue
            else:
                result += int(sign+temp)
                temp = ''
            sign = x
        else:
            temp += x

    result += int(sign+temp)
    return result

# s = '25-4+1' #22
# s = '-3+26-7' #16
s = '7-24+9' #-8
result = solution(s)
print(result)