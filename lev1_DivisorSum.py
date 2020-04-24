#약수의 합
#추천 많은 풀이

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

"""
나의풀이
    def solution(n):
        sum = 0
        for i in range(1,n+1):
            if n % i == 0:
                sum += i
        return sum
"""
