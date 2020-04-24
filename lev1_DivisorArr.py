#나누어 떨어지는 숫자 배열

#추천이 제일 많았던 풀이 
#이해는 가나 sorted 안에 [] 쓸 때 맨앞으 n 을 주는이유
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

"""
나의 풀이

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer = [-1]
    return sorted(answer)
"""
