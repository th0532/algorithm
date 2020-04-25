#x만큼 간격이 있는 n개의 숫자
#추천 많은 풀이
def solution(x, n):
    return [i * x + x for i in range(n)]


"""
나의풀이
def solution(x, n):
    answer = []
    plus = x
    for i in range(n):
        answer.append(x)
        x += plus
    return answer


"""