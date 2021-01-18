# 1
def solution(array, commands):
    answer = []
    sortedArray = []
    
    for i in range(len(commands)):
        a=[]
        for j in range(commands[i][0], commands[i][1]+1):
            a.append(array[j-1])
        a.sort()
        sortedArray.append(a)
    for i in range(len(commands)):
        answer.append(sortedArray[i][commands[i][2]-1])
    return answer

# 2
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer