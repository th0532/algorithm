# K번째수
#추천 많이 받은 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""
나의 풀이

def solution(array, commands):
    _result = []
    for ab in commands:
        i, j, k = ab
        _result.append(sorted(array[i-1:j])[k-1])
    return _result
"""