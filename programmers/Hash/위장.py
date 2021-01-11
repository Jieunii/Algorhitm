from collections import Counter
from functools import reduce
def solution(clothes):
    answer = 0
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x,y: x*(y+1), cnt.values(), 1)
    return answer-1