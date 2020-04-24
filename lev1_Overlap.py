# 같은 숫자는 싫어
# 추천이 많은 풀이
# list에 마지막값이랑 for i 랑 비교해서 같으면 continue 다르면 append ,,,,good
def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 나의 풀이
"""
def solution(arr):
    b =[]
    b.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            b.append(arr[i])
    
    return b
"""
