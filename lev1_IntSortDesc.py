#정수 내림차순으로 배치하기
#추천이 제일 많았던 풀이 

def solution(n):
    ls = list(str(n))
    ls = sorted(ls, reverse = True)
    return int("".join(ls))

"""
나의 풀이

    def solution(n):
        txt = ""
    for i in sorted(str(n), reverse = True):
        txt += i

    return int(txt)
"""