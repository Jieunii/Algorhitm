def solution(priorities, location):
    p = []
    index = [i for i in range(len(priorities))]
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            p.append(index.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            index.append(index.pop(0))

    return p.index(location) + 1