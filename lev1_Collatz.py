# 콜라츠 추측
def solution(num):
    _count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            _count = _count+1
        elif num % 2 == 1:
            num = (num*3) + 1
            _count = _count+1
        if 500<=_count:
            _count = -1
            break
            
    return _count