#완주하지 못한선수
import collections

def solution(participant, completion):
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]