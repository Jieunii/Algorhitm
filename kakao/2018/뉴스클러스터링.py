def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]

    inter = set(str1) & set(str2)
    uni = set(str1) | set(str2)

    if len(uni) == 0:
        return 65536

    inter_sum = sum([min(str1.count(i), str2.count(i)) for i in inter])
    uni_sum = sum([max(str1.count(u), str2.count(u)) for u in uni])

    return int((inter_sum/uni_sum)*65536)