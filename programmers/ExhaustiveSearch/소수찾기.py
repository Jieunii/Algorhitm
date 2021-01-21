import itertools

def solution(numbers):
    arr = list(numbers)
    per = []
    for i in range(len(numbers)):
        per.extend(list(map(''.join, itertools.permutations(arr, i+1))))
    per = [int(i) for i in per]
    number = list(set(per))
    primeNum = 0
    for i in number:
        if i%2 != 0:
            odd = i
            cnt = 0
            for divide in range(1, odd+1):
                if odd % divide  == 0:
                    cnt += 1
                    if cnt > 2:
                        break
            if cnt == 2:
                primeNum += 1
        elif i == 2:
            primeNum += 1
    return primeNum
