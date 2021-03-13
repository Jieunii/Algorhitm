from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    
    # infos 처리
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_category = info[:-1]
        info_score = int(info[-1])
        
        # 점수를 제외한 16가지 조합
        for i in range(5):
            for c in combinations(info_category, i):
                key = ''.join(c)
                info_dict[key].append(info_score)
    
    # 점수 정렬
    for key in info_dict.keys():
        info_dict[key].sort()
    
    # queries 처리
    for query in queries:
        qu = []
        query = query.split()
        
        for q in query:
            if q != 'and' and q != '-':
                qu.append(q)
        key = ''.join(qu[:-1])
        score = int(qu[-1])
        
        # 이분탐색으로 지원자 수 구하기
        count = 0
        if key in info_dict.keys():
            value = info_dict[key]
            start, end = 0, len(value)
            while start <= end and start < len(value):
                mid = (start+end)//2
                if value[mid] < score:
                    start = mid+1
                else:
                    end = mid-1
            count = len(value)-start
        answer.append(count)
                    
    return answer