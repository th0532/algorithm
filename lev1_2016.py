#2016

#추천이 제일 많았던 풀이 
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

"""
나의 풀이
비효율 적임 ,,,, 나중에 다시 풀어보기
def solution(a, b):
    #1~12월 일수
    days = [0,31,60,91,121,152,182,213,244,274,305,335,366]
    date_sum = days[a-1] +b
    print (date_sum)

    _result = date_sum % 7
    print (_result)
        
    if _result == 0:
        return "THU"
    elif _result == 1:
        return "FRI"
    elif _result == 2:
        return "SAT"
    elif _result == 3:
        return "SUN"
    elif _result == 4:
        return "MON"
    elif _result == 5:
        return "TUE"
    elif _result == 6:
        return "WED"
"""
