def solution(answers):
    good = []
    supo1 = itertools.cycle([1, 2, 3, 4, 5])
    supo2 = itertools.cycle([2, 1, 2, 3, 2, 4, 2, 5])
    supo3 = itertools.cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for i in range(len(answers)):
        if supo1[i] == answers[i]: cnt1 += 1
        if supo2[i] == answers[i]: cnt2 += 1
        if supo3[i] == answers[i]: cnt3 += 1
    math = [cnt1, cnt2, cnt3]
    MAX = max(math)
    if MAX == cnt1: good.append(1)
    if MAX == cnt2: good.append(2)
    if MAX == cnt3: good.append(3)
    return good