#자릿수 더하기
#추천 많은 1. #재귀함수
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

#추천 2   
def sum_digit(number):
    return sum([int(i) for i in str(number)])
    
#추천3
def solution(n):
    return sum(map(int, str(n)))



"""
나의풀이
def solution(n):
    _result = 0
    for i in str(n):
        _result += int(i)       
    return _result

"""