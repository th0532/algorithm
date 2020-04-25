#카카오 비밀지도
#추천 많은 풀이
def solution(n, arr1, arr2):
    ls = []
    # or 비트연산자 -> 16자리 2진법 -> n의 자리로 -> replace -> return
    for i in range (n):
        _res10 = arr1[i] | arr2[i]
        _resBin = bin(_res10)[2:].rjust(n,"0")
        _resBin = _resBin.replace ("1","#")
        _resBin = _resBin.replace ("0"," ")
        ls.append(_resBin)
    return ls


"""
나의풀이
def solution(n, arr1, arr2):
    ls = []
    # or 비트연산자 -> 16자리 2진법 -> n의 자리로 -> replace -> return
    for i in range (n):
        _res10 = arr1[i] | arr2[i]
        _resBin = bin(_res10)[2:].rjust(n,"0")
        _resBin = _resBin.replace ("1","#")
        _resBin = _resBin.replace ("0"," ")
        ls.append(_resBin)
    return ls


"""