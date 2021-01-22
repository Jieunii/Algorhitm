def solution(brown, yellow):
    number = brown + yellow
    answer = [0] * 2
    for garo in range(1, number+1):
        if number % garo == 0:
            sero = number / garo
            if ((sero-2)*(garo-2) == yellow) & (garo >= sero):
                answer[0] = garo
                answer[1] = sero
    return answer