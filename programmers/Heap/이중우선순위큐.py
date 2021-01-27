import heapq

def solution(operations):
    answer = []
    length = len(operations)
    oper = []
    numbers = []
    for i in range(length):
        tmp = []
        tmp.extend(operations[i].split(' '))
        oper.append(tmp)
    for i in range(len(oper)):
        if oper[i][0] == 'I':
            numbers.append(int(oper[i][1]))
        else:
            if len(numbers) != 0:
                if oper[i][1] == '-1':
                    numbers.remove(min(numbers))
                else:
                    numbers.remove(max(numbers))
    if len(numbers) != 0:
        answer = [max(numbers), min(numbers)]
    else:
        answer = [0, 0]
    return answer