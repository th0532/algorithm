#가운데 글자 가져오기

#추천이 제일 많았던 풀이 
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

"""
나의 풀이
def solution(s):

    pevot = int(len(s)/2)
    print (pevot)

    if len(s) % 2 == 0:
        return s[pevot-1:pevot+1]
    else:
        return s[pevot]
"""
