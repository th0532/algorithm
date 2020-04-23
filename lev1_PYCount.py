#문자열 내 p와 y의 개수
#추천이 제일 많았던 풀이 //lower -> 소문자 -> count
def solution(s):
    return s.lower().count("p") == s.lower().count("y")

"""
나의 풀이
def solution(s):
    answer = True
    p_count = 0
    y_count = 0


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for i in s:
        if("p" in i or "P" in i):   #p와 P 가 i 에 있는지 check 후 count +1
            p_count = p_count+1
        
        if("y" in i or "Y" in i):   #y와 Y 가 i 에 있는지 check 후 count +1
            y_count = y_count+1
    
    if p_count == y_count:
        return True
    else:
        return 0
"""