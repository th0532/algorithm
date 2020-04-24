#문자열다루기 기본

#추천이 제일 많았던 풀이 
def solution(s):
    return s.isdigit() and len(s) in (4,6)

"""
나의풀이
    def solution(s):
         if len(s) == 4 or len(s) ==6:
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True
    else :
        return False
"""