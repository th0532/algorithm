#행렬의 덧셈
#추천 많은 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

"""
나의풀이
def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        tmp = []
        for c,d in zip(a,b):
            tmp.append(c+d)
        answer.append(tmp)
    return answer


"""