#수박수박수박수박수박수?
#추천이 제일 많았던 풀이 
def water_melon(n):
    s = "수박" * n
    return s[:n]    #n까지 slicing ,,,,, 

"""
나의 풀이

def solution(n):
    a = ""
    for i in range(n):
        if i % 2 == 0:
            a += "수"
        else :
            a += "박"
    return a
"""