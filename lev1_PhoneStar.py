# 핸드폰 번호 가리기
# 추천많은 수,, 문자열도 * 이 가능하다,,,
def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4:]

"""
나의풀이
def solution(phone_number):
    txt = ""
    for i in range (len(phone_number[0:-4])):
        txt += "*"
    txt += phone_number[-4:]
    return txt
"""