def solution(record):
    answer = []
    result = []
    chat = [rec.split() for rec in record]
    info = {}
    for ch in chat:
        if ch[0] == 'Enter':
            info[ch[1]] = ch[2]
            answer.append([ch[1], 'Enter'])
        elif ch[0] == 'Leave':
            answer.append([ch[1], 'Leave'])
        else:
            info[ch[1]] = ch[2]
    
    for i in answer:
        if i[1] == 'Enter':
            result.append('{}님이 들어왔습니다.'.format(info[i[0]]))
        else:
            result.append('{}님이 나갔습니다.'.format(info[i[0]]))
            
    return result