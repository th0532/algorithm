#하샤드 수
#추천 많은 풀이
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

"""
나의풀이
def Harshad(n):
    _sum = 0
    for i in str(n):
        _sum += int(i)
    return n % hap == 0
"""